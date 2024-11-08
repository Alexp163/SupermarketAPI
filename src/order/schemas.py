from datetime import datetime

from pydantic import BaseModel

class OrderReadSchema(BaseModel):
    id: int
    price: float
    date_order: datetime
    customer_id: int
    worker_id: int
    food_id: int
    product_id: int
    created_at: datetime
    updated_at: datetime


class OrderCreateSchema(BaseModel):
    price: float
    date_order: datetime
    customer_id: int
    worker_id: int
    food_id: int
    product_id: int


class OrderUpdateSchema(BaseModel):
    price: float
    date_order: datetime
    customer_id: int
    worker_id: int
    food_id: int
    product_id: int


