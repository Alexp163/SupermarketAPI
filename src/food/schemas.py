from datetime import datetime
from pydantic import BaseModel


class FoodReadSchema(BaseModel):
    id: int
    name: str
    prime: float
    expiration_date: datetime
    created_at: datetime
    updated_at: datetime


class FoodCreateSchema(BaseModel):
    name: str
    prime: float
    expiration_date: datetime


class FoodUpdateSchema(BaseModel):
    name: str
    prime: float
    expiration_date: datetime


