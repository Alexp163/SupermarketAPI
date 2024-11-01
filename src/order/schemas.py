from datetime import datetime

from pydantic import BaseModel

class OrderReadSchema(BaseModel):
    id: int
    price: float
    date_order: datetime
    created_at: datetime
    updated_at: datetime


class OrderCreateSchema(BaseModel):
    price: float
    date_order: datetime


class OrderUpdateSchema(BaseModel):
    price: float
    date_order: datetime