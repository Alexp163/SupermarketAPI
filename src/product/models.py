from datetime import datetime
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql import func

from database import Base


class Product(Base):  # продукт
    __tablename__ = "product"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()  # название продукта
    expiration_date: Mapped[datetime] = mapped_column()  # срок годности продукта
    price: Mapped[float] = mapped_column()  # цена товара
    balance: Mapped[int] = mapped_column()  # остаток товара на складе

    created_at: Mapped[datetime] = mapped_column(server_default=func.now())  # дата создания
    updated_at: Mapped[datetime] = mapped_column(server_default=func.now(), onupdate=func.now())  # дата обновления

    def __repr__(self):
        return f"{self.id} {self.name} {self.expiration_date} {self.price} {self.balance}"

