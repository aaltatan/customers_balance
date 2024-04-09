from ninja import Router
from ninja.pagination import paginate, LimitOffsetPagination
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest
from typing import List
from . import schemas
from .models import Transaction
from ..customers.models import Customer
from django.db.models import Sum, F, Window, Count, Q
from django.db.models.functions import LastValue
from django.contrib import messages


router = Router(
    tags=['Transactions']
)


@router.get("/", response=List[schemas.TransactionSchema])
@paginate(LimitOffsetPagination)
def get_transactions(request: HttpRequest):
    transactions = (
        Transaction
        .objects
        .annotate(
            amount=F('debit') - F('credit'),
            running_net=Window(
                expression=Sum(F('debit') - F('credit')),
                order_by='added_at'
            )
        )   
        .order_by('-added_at')
    )
    return transactions


@router.get('/balance', response=List[schemas.BalanceSchema])
def get_balance(
    request: HttpRequest, 
    keyword: str | None = None,
    show_all: int = 0,
    order_by: str = 'customer__name'
):

    stmt_keyword = Q(customer__name__contains=keyword) if keyword else Q()
    stmt_show_all = Q() if show_all else ~Q(customer_net=0)
    stmt = stmt_keyword & stmt_show_all

    balance = (
        Transaction
        .objects
        .values('customer__name','customer__id')
        .annotate(
            last_date=Window(
                expression=LastValue('date'),
                partition_by='customer__name',
            ),
            customer_net=Window(
                Sum(F('debit') - F('credit')),
                partition_by='customer__name'
            ),
            transactions_count=Window(
                Count('debit'),
                partition_by='customer__name'
            )
        )
        .distinct()
        .filter(stmt)
        .order_by(order_by)
    )

    return balance


@router.get('/report')
def get_report(request: HttpRequest):
    report = (
        Transaction
        .objects
        .aggregate(
            total_debit=(Sum('debit')),
            total_credit=(Sum('credit')),
            net=(Sum(F('debit') - F('credit'))),
            transactions_count=Count('debit'),
        )
    )
    customers_count = (
        Customer
        .objects
        .aggregate(
            customers_count=Count('name')
        )
    )

    report = {**report, **customers_count}
    return report


@router.get('/ledger/{id}', response=List[schemas.LedgerSchema])
def get_ledger(request: HttpRequest, id:int):
    ledger = (
        Transaction
        .objects
        .filter(customer__id=id)
        .annotate(
            running_net=Window(
            expression=Sum(F('debit') - F('credit')),
            order_by='added_at'
            ),
            amount=F('debit') - F('credit')
        )
    )
    return ledger



@router.post('/add', response={201: None})
def add_transaction(request: HttpRequest, 
                    payload: schemas.TransactionInSchema):
    customer = (
        Customer
        .objects
        .filter(id__exact=payload.customer)
        .first()
    )
    Transaction.objects.create(**{
        'customer': customer,
        'user': request.user,
        payload.type: payload.amount,
    })
    messages.success(
        request=request, 
        message='Transaction has been added successfully'
    )
    return 201, None

