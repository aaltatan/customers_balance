from django.contrib import messages
from django.http import HttpRequest
from excel_response import ExcelResponse
from ninja import Router
from ninja.pagination import LimitOffsetPagination, paginate

from apps.customers.models import Customer

from . import schemas
from .models import Transaction

router = Router(tags=["Transactions"])


@router.get("/", response=list[schemas.TransactionSchema])
@paginate(LimitOffsetPagination)
def get_transactions(_: HttpRequest):
    return Transaction.objects.annotate_running_net().annotate_amount().order_by("-added_at")


@router.get("/excel")
def export_transactions_to_excel(_: HttpRequest):
    transactions = (
        Transaction.objects.annotate_running_net()
        .annotate_customer_name()
        .annotate_user_username()
        .order_by("added_at")
    )
    return ExcelResponse(transactions)


@router.get("/balance", response=list[schemas.BalanceSchema])
def get_balance(
    _: HttpRequest, keyword: str | None = None, show_all: int = 0, order_by: str = "customer__name"
):
    Transaction.objects.get_balance(keyword, show_all, order_by)


@router.get("/report")
def get_report(_: HttpRequest):
    report = Transaction.objects.get_report()
    customers_count = Customer.objects.get_customers_count()
    return {**report.asdict(), "customers_count": customers_count}


@router.get("/ledger/{customer_id}", response=list[schemas.LedgerSchema])
def get_ledger(_: HttpRequest, customer_id: int):
    return (
        Transaction.objects.filter(customer__id=customer_id)
        .annotate_running_net()
        .annotate_amount()
        .all()
    )


@router.get("/ledger/excel/{customer_id}")
def export_ledger(_: HttpRequest, customer_id: int):
    ledger = (
        Transaction.objects.filter(customer__id=customer_id)
        .annotate_customer_name()
        .annotate_user_username()
        .annotate_running_net()
    )
    return ExcelResponse(ledger)


@router.post("/add", response={201: None})
def add_transaction(request: HttpRequest, payload: schemas.TransactionInSchema):
    customer = Customer.objects.filter(id__exact=payload.customer).first()
    Transaction.objects.create(
        **{"customer": customer, "user": request.user, payload.type: payload.amount}
    )
    messages.success(request=request, message="Transaction has been added successfully")
    return 201, None
