from datetime import datetime

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql import func

from database import Base


class Position(Base):
    __tablename__ = "position"

    id: Mapped[int] = mapped_column(primary_key=True)

    quantity: Mapped[int] = mapped_column()
    order = relationship("Order")
    order_id: Mapped[int | None] = mapped_column(ForeignKey("order.id"))
    food = relationship("Food")
    food_id: Mapped[int | None] = mapped_column(ForeignKey("food.id"))
    product = relationship("Product")
    product_id: Mapped[int | None] = mapped_column(ForeignKey("product.id"))

    created_at: Mapped[datetime] = mapped_column(server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(server_default=func.now(), onupdate=func.now())

    def __repr__(self):
        return f"{self.id} {self.quantity} {self.order_id} {self.food_id} {self.product_id}"


