from django.http import HttpRequest
from excel_response import ExcelResponse
from ninja import Router

from . import schemas
from .models import Customer

router = Router(tags=["Customers"])


@router.get("/excel")
def export_customers_to_excel(_: HttpRequest):
    """Export customers to excel."""
    return ExcelResponse(
        Customer.objects.annotate_transactions_count().annotate_net().all(), "customers"
    )


@router.post("/add", response=schemas.CustomerOutSchema)
def add_customer(_: HttpRequest, payload: schemas.CustomerInSchema):
    """Add new customer."""
    return Customer.objects.create(**payload.model_dump())


@router.get("/{customer_id}", response=schemas.NewCustomerSchema)
def get_customer_by_id(_: HttpRequest, customer_id: int):
    """Get customer by <strong>id</strong>."""
    return (
        Customer.objects.filter(pk=customer_id)
        .annotate_total_debit()
        .annotate_total_credit()
        .annotate_net()
        .first()
    )


@router.post("/", response={204: None, 409: None})
def get_customer_by_name(_: HttpRequest, customer: schemas.CustomerInSchema):
    """Get customer by <strong>name</strong>."""
    customer_exists = Customer.objects.filter(name__exact=customer.name).first()

    if customer_exists:
        return 409, None

    return 204, None


@router.get("/search/{keyword}", response=list[schemas.CustomerOutSchema])
def search(_: HttpRequest, keyword: str):
    """Search for customer bu name."""
    return Customer.objects.filter(name__contains=keyword)
