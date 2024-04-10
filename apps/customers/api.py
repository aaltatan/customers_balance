from ninja import Router
from django.http import HttpRequest
from typing import List
from . import schemas
from .models import Customer
from django.db.models import Sum, F, Count
from excel_response import ExcelResponse


router = Router(
    tags=['Customers']
)


@router.get('/excel')
def export_customers_to_excel(request: HttpRequest):
    """ export customers to excel """
    customers = (
        Customer
        .objects
        .annotate(
            net=Sum(F("transaction__debit") - F("transaction__credit")),
            transactions_count=Count('transaction__debit')
        )
    )
    return ExcelResponse(customers, 'customers')


@router.post(
    "/add", 
    response=schemas.CustomerOutSchema,
)
def add_customer(request: HttpRequest, payload: schemas.CustomerInSchema):
    """ add new customer """

    customer = Customer.objects.create(**payload.model_dump())
    return customer


@router.get("/{customer_id}", response=schemas.NewCustomerSchema)
def get_customer_by_id(request: HttpRequest, customer_id: int):
    """get customer by <strong>id</strong>"""
    
    return (
        Customer.objects.filter(pk=customer_id)
        .annotate(
            debit=Sum("transaction__debit"),
            credit=Sum("transaction__credit"),
            net=Sum(F("transaction__debit") - F("transaction__credit")),
        )
        .first()
    )


@router.post("/", response={204: None, 409: None})
def get_customer_by_name(request: HttpRequest, 
                       customer: schemas.CustomerInSchema):
    """get customer by <strong>name</strong>"""

    customer_exists = (
        Customer
        .objects
        .filter(name__exact=customer.name)
        .first()
    )
    if customer_exists:
        return 409, None
    
    return 204, None


@router.get("/search/{keyword}", response=List[schemas.CustomerOutSchema])
def search(request: HttpRequest, keyword: str):
    """ search for customer bu name """
    
    customers = Customer.objects.filter(name__contains=keyword)
    return customers
