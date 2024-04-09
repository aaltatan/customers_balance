from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError
from ..customers.models import Customer


amount_validators = [MinValueValidator(0, "must be equal or more than 0")]


class Transaction(models.Model):
    added_at = models.DateTimeField(auto_now_add=True)
    last_edit = models.DateTimeField(auto_now=True)
    date = models.DateTimeField(default=datetime.now)
    debit = models.IntegerField(default=0, validators=amount_validators)
    credit = models.IntegerField(default=0, validators=amount_validators)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.customer.name} (debit={self.debit}, credit={self.credit})"

    def clean(self) -> None:
        if self.debit == 0 and self.credit == 0:
            raise ValidationError("you must fill debit or credit")
        if self.debit != 0 and self.credit != 0:
            raise ValidationError("you must fill debit or credit")
