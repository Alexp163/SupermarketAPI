from datetime import datetime

from pydantic import BaseModel


class CustomerReadSchema(BaseModel):
    id: int
    name: str
    age: int
    rating: float
    created_at: datetime
    updated_at: datetime


class CustomerCreateSchema(BaseModel):
    name: str
    age: int
    rating: float


class CustomerUpdateSchema(BaseModel):
    name: str
    age: int
    rating: float




