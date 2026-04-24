from datetime import datetime

from ninja import Field, Schema
from ninja.errors import ValidationError
from pydantic import field_validator

from apps.customers.schemas import CustomerOutSchema


class UserSchema(Schema):
    id: int
    username: str
    first_name: str | None = None
    last_name: str | None = None


class TransactionSchema(Schema):
    added_at: datetime
    last_edit: datetime
    date: datetime
    debit: int
    credit: int
    customer: CustomerOutSchema
    user: UserSchema
    running_net: int
    amount: int


class LedgerSchema(TransactionSchema):
    id: int


class TransactionInSchema(Schema):
    amount: int = Field(default=0)
    type: str
    customer: int

    @field_validator("amount")
    @classmethod
    def validate_amount(cls, value: int) -> int:
        if value <= 0:
            raise ValidationError(
                [
                    {
                        "msg": "must be more than 0",
                        "type": "value",
                        "loc": ["amount"],
                    }
                ]
            )
        return value


class BalanceSchema(Schema):
    customer__name: str
    customer__id: int
    customer_net: int
    transactions_count: int
    last_date: datetime
