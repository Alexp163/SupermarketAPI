from datetime import datetime

from pydantic import BaseModel

class OrderReadSchemas(BaseModel):
    id: int
    price: float
    date_order: datetime
    created_at: datetime
    updated_at: datetime


class OrderCreateSchemas(BaseModel):
    price: float
    date_order: datetime


class OrderUpdateSchemas(BaseModel):
    price: float
    date_order: datetime