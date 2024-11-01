from datetime import datetime

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql import func

from database import Base

class Order(Base):  # заказ
    __tablename__ = "order"

    id: Mapped[int] = mapped_column(primary_key=True)
    price: Mapped[float] = mapped_column() # стоимость заказа
    date_order: Mapped[datetime] = mapped_column()  # дата заказа
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(server_default=func.now(), onupdate=func.now())

    def __repr__(self):
        return f"{self.price} {self.date_order} "

