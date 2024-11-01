from datetime import datetime

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql import func

from database import Base


class Food(Base):  # пищевые продукты
    __tablename__ = "food"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()  # название продукта
    price: Mapped[float] = mapped_column()  # цена продукта
    expiration_date: Mapped[datetime] = mapped_column()  # срок годности
    balance: Mapped[int] = mapped_column()  # остаток на складе
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(server_default=func.now(), onupdate=func.now())

    def __repr__(self):
        return f"{self.name} {self.price} {self.expiration_date} {self.balance}"


