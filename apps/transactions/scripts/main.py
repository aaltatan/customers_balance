from ..models import Transaction
from ...customers.models import Customer
from django.db.models import Sum, F, Window, Count, Q, Value as V
from django.db.models.functions import LastValue
from django.db import models
from datetime import datetime
import re


def run():

    customers = (
        Customer
        .objects
        .annotate(net=Sum(F("transaction__debit") - F("transaction__credit")))
        .values()
    )

    for c in customers:
        print(c)
        print("#" * 100)
