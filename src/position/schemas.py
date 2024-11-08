from datetime import datetime

from pydantic import BaseModel

class PositionReadSchema(BaseModel):
    id: int
    quantity: int
    order_id: int
    food_id: int
    product_id: int
    created_at: datetime
    updated_at: datetime


class PositionCreateSchema(BaseModel):
    quantity: int
    order_id: int
    food_id: int
    product_id: int


class PositionUpdateSchema(BaseModel):
    quantity: int
    order_id: int
    food_id: int
    product_id: int

