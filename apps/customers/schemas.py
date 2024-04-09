from ninja import Schema
from pydantic import validator
import re


class CustomerBase(Schema):
    name: str


class CustomerInSchema(CustomerBase):
    @validator("name")
    @classmethod
    def validate_name(cls, val):
        pattern = re.compile(r"\s{2,}")
        saved_name = pattern.sub(" ", val)
        val = " ".join(word.capitalize() for word in saved_name.split(" "))
        return val


class CustomerOutSchema(CustomerBase):
    id: int


class NewCustomerSchema(CustomerOutSchema):
    net: int
