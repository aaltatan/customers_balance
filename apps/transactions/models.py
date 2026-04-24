from dataclasses import asdict, dataclass
from datetime import datetime
from typing import Any, ClassVar

from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from django.db import models
from django.db.models import Count, F, Sum, Window
from django.db.models.functions import LastValue
from django.db.models.query import ValuesQuerySet

from apps.customers.models import Customer


@dataclass
class _Report:
    total_debit: int
    total_credit: int
    net: int
    transactions_count: int

    def asdict(self) -> dict:
        return asdict(self)


class TransactionQuerySet(models.QuerySet):
    def annotate_running_net(self) -> "TransactionQuerySet":
        return self.annotate(
            running_net=Window(
                expression=Sum(F("debit") - F("credit")), order_by=models.F("added_at")
            )
        )

    def annotate_amount(self) -> "TransactionQuerySet":
        return self.annotate(amount=F("debit") - F("credit"))

    def annotate_customer_name(self) -> "TransactionQuerySet":
        return self.annotate(customer_name=F("customer__name"))

    def annotate_customer_net(self) -> "TransactionQuerySet":
        return self.annotate(
            customer_net=Window(Sum(F("debit") - F("credit")), partition_by="customer__name"),
        )

    def annotate_transactions_count(self) -> "TransactionQuerySet":
        return self.annotate(transactions_count=Count("debit"))

    def annotate_last_date(self) -> "TransactionQuerySet":
        return self.annotate(
            last_date=Window(expression=LastValue("date"), partition_by="customer__name")
        )

    def annotate_user_username(self) -> "TransactionQuerySet":
        return self.annotate(user_username=F("user__username"))


class TransactionManager(models.Manager):
    def get_queryset(self) -> TransactionQuerySet:
        return TransactionQuerySet(self.model, using=self._db)

    def annotate_running_net(self) -> TransactionQuerySet:
        return self.get_queryset().annotate_running_net()

    def annotate_amount(self) -> TransactionQuerySet:
        return self.get_queryset().annotate_amount()

    def annotate_customer_name(self) -> TransactionQuerySet:
        return self.get_queryset().annotate_customer_name()

    def annotate_customer_net(self) -> TransactionQuerySet:
        return self.get_queryset().annotate_customer_net()

    def annotate_transactions_count(self) -> TransactionQuerySet:
        return self.get_queryset().annotate_transactions_count()

    def annotate_last_date(self) -> TransactionQuerySet:
        return self.get_queryset().annotate_last_date()

    def annotate_user_username(self) -> TransactionQuerySet:
        return self.get_queryset().annotate_user_username()

    def get_report(self) -> _Report:
        data = self.get_queryset().aggregate(
            total_debit=(Sum("debit")),
            total_credit=(Sum("credit")),
            net=(Sum(F("debit") - F("credit"))),
            transactions_count=Count("debit"),
        )
        return _Report(**data)

    def get_balance(
        self, keyword: str | None, show_all: int, order_by: str
    ) -> ValuesQuerySet[Any, dict[str, Any]]:
        query = (
            Transaction.objects.values("customer__name", "customer__id")
            .annotate(
                last_date=Window(expression=LastValue("date"), partition_by="customer__name"),
                customer_net=Window(Sum(F("debit") - F("credit")), partition_by="customer__name"),
                transactions_count=Window(Count("debit"), partition_by="customer__name"),
            )
            .distinct()
        )

        if keyword:
            query = query.filter(customer__name__contains=keyword)

        if show_all:
            query = query.filter(~models.Q(customer_net=0))

        return query.order_by(order_by)


class Transaction(models.Model):
    added_at = models.DateTimeField(
        auto_now_add=True,
    )
    last_edit = models.DateTimeField(
        auto_now=True,
    )
    date = models.DateTimeField(
        default=datetime.now,
    )
    debit = models.IntegerField(
        default=0,
        validators=[
            MinValueValidator(0, "must be equal or more than 0"),
        ],
    )
    credit = models.IntegerField(
        default=0,
        validators=[
            MinValueValidator(0, "must be equal or more than 0"),
        ],
    )
    customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE,
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )

    objects: ClassVar[TransactionManager] = TransactionManager()  # type: ignore  # noqa: PGH003

    def __str__(self) -> str:
        return f"{self.customer.name} (debit={self.debit}, credit={self.credit})"

    def clean(self) -> None:
        error_rules = [
            (lambda: self.debit > self.credit, "debit must be equal or less than credit"),
            (lambda: self.debit != 0 and self.credit != 0, "you must fill debit or credit"),
        ]
        for rule, message in error_rules:
            if rule():
                raise ValidationError(message)
