import re

from ninja import Schema
from pydantic import field_validator


class CustomerBase(Schema):
    name: str


class CustomerInSchema(CustomerBase):
    @field_validator("name")
    @classmethod
    def validate_name(cls, val: str) -> str:
        pattern = re.compile(r"\s{2,}")
        saved_name = pattern.sub(" ", val)
        return " ".join(word.capitalize() for word in saved_name.split(" "))


class CustomerOutSchema(CustomerBase):
    id: int


class NewCustomerSchema(CustomerOutSchema):
    net: int
