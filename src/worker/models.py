from datetime import datetime

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql import func

from database import Base


class Worker(Base):
    __tablename__ = "worker"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()  # ФИО сотрудника
    profile: Mapped[str] = mapped_column()  # профиль работы
    age: Mapped[int] = mapped_column()  # возраст сотрудника
    experience: Mapped[int] = mapped_column()  # опыт работы сотрудника

    created_at: Mapped[datetime] = mapped_column(server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(server_default=func.now(), onupdate=func.now())

    def __repr__(self):
        return f"{self.id} {self.name} {self.profile} {self.age} {self.experience}"
