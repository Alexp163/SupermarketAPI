from datetime import datetime

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql import func

from database import Base

class Order(Base):  # заказ
    __tablename__ = "order"

    id: Mapped[int] = mapped_column(primary_key=True)
    price: Mapped[float] = mapped_column() # стоимость заказа
    customer: Mapped["Customer"] = relationship("Customer")  # заказчик
    customer_id: Mapped[int | None] = mapped_column(ForeignKey("customer.id"))
    worker: Mapped["Worker"] = relationship("Worker")  # ответственный за заказ
    worker_id: Mapped[int | None] = mapped_column(ForeignKey("worker.id"))
    food: Mapped["Food"] = relationship("Food")  # пищевые продукты в заказе
    food_id: Mapped[int | None] = mapped_column(ForeignKey("food.id"))
    product: Mapped["Product"] = relationship("Product")  # непищевые продукты в заказе
    product_id: Mapped[int | None] = mapped_column(ForeignKey("product.id"))
    date_order: Mapped[datetime] = mapped_column()  # дата заказа
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(server_default=func.now(), onupdate=func.now())

    def __repr__(self):
        return f"{self.price} {self.date_order} {self.customer_id} {self.worker_id} {self.food_id} {self.product_id}"


