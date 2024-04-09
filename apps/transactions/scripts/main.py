from ..models import Transaction
from ...customers.models import Customer
from django.db.models import Sum, F, Window, Count, Q, Value as V
from django.db.models.functions import LastValue
from django.db import models
from datetime import datetime
import re


def run():
  
    pattern = re.compile(r'\s{2,}')
    name = 'Adad   dasd fsdf       dasd'
    

    print(pattern.sub(" ", name))