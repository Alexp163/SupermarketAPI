from pydantic import BaseModel
from datetime import datetime

class ProductReadSchema(BaseModel):
    id: int
    name: str # название продукта
    expiration_date: datetime  # срок годности
    price: float  # цена продукта
    balance: int  # фактический остаток
    created_at: datetime  # дата создания
    updated_at: datetime  # дата обновления


class ProductCreateSchema(BaseModel):
    name: str
    expiration_date: datetime
    price: float
    balance: int


class ProductUpdateSchema(BaseModel):
    name: str
    expiration_date: datetime
    price: float
    balance: int

