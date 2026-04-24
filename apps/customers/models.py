import re
from typing import Any, ClassVar

from django.db import models


class CustomerQuerySet(models.QuerySet):
    def annotate_transactions_count(self) -> "CustomerQuerySet":
        return self.annotate(transactions_count=models.Count("transaction"))

    def annotate_total_debit(self) -> "CustomerQuerySet":
        return self.annotate(total_debit=models.Sum("transaction__debit"))

    def annotate_total_credit(self) -> "CustomerQuerySet":
        return self.annotate(total_credit=models.Sum("transaction__credit"))

    def annotate_net(self) -> "CustomerQuerySet":
        return self.annotate(
            net=models.Sum(models.F("transaction__debit") - models.F("transaction__credit"))
        )


class CustomerManager(models.Manager):
    def get_queryset(self) -> CustomerQuerySet:
        return CustomerQuerySet(self.model, using=self._db)

    def annotate_transactions_count(self) -> CustomerQuerySet:
        return self.get_queryset().annotate_transactions_count()

    def annotate_total_debit(self) -> CustomerQuerySet:
        return self.get_queryset().annotate_total_debit()

    def annotate_total_credit(self) -> CustomerQuerySet:
        return self.get_queryset().annotate_total_credit()

    def annotate_net(self) -> CustomerQuerySet:
        return self.get_queryset().annotate_net()

    def get_customers_count(self) -> int:
        return self.get_queryset().count()


class Customer(models.Model):
    added_at = models.DateTimeField(
        auto_now_add=True,
    )
    last_edit = models.DateTimeField(
        auto_now=True,
    )
    name = models.CharField(
        max_length=255,
        unique=True,
    )

    objects: ClassVar[CustomerManager] = CustomerManager()  # type: ignore  # noqa: PGH003

    def __str__(self) -> str:
        return self.name

    def save(self, *args: Any, **kwargs: Any) -> Any:
        pattern = re.compile(r"\s{2,}")
        saved_name = pattern.sub(" ", self.name)
        self.name = " ".join(word.capitalize() for word in saved_name.split(" "))
        return super().save(*args, **kwargs)
