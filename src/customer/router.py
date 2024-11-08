from fastapi import APIRouter, Depends, status
from sqlalchemy import delete, insert, select, update

from database import get_async_session
from .models import Customer
from .schemas import CustomerCreateSchema, CustomerReadSchema, CustomerUpdateSchema

router = APIRouter(tags=["customers"], prefix="/customers")

@router.post("/", status_code=status.HTTP_201_CREATED)  # 1) создание покупателя
async def create_customer(customer: CustomerCreateSchema, session=Depends(get_async_session)) -> CustomerReadSchema:
    statement = insert(Customer).values(
        name=customer.name,
        age=customer.age,
        rating=customer.rating
    ).returning(Customer)
    result = await session.scalar(statement)
    await session.commit()
    return result


@router.get("/", status_code=status.HTTP_200_OK)  # 2) получает данные о всех пользователях
async def get_customer(max_age: int | None = None,
                       min_age: int | None = None,
                       max_rating: float | None = None,
                       min_rating: float | None = None,
                       session=Depends(get_async_session)) -> list[CustomerReadSchema]:
    statement = select(Customer)
    if max_age is not None:
        statement = statement.where(Customer.age <= max_age)
    if min_age is not None:
        statement = statement.where(Customer.age >= min_age)
    if max_rating is not None:
        statement = statement.where(Customer.rating <= max_rating)
    if min_rating is not None:
        statement = statement.where(Customer.rating >= min_rating)
    result = await session.scalars(statement)
    return list(result)


@router.get("/{customer_id}", status_code=status.HTTP_200_OK)  # 3) получает данные о покупателе по id
async def get_customer_by_id(customer_id: int, session=Depends(get_async_session)) -> CustomerReadSchema:
    statement = select(Customer).where(Customer.id == customer_id)
    result = await session.scalar(statement)
    return result


@router.delete("/{customer_id}", status_code=status.HTTP_200_OK)  # 4) удаление покупателя по id
async def delete_customer_bs_id(customer_id: int, session=Depends(get_async_session)) -> None:
    statement = delete(Customer).where(Customer.id == customer_id)
    await session.execute(statement)
    await session.commit()


@router.put("/{customer_id}", status_code=status.HTTP_200_OK)  # 5) обновление данных о покупателе по id
async def update_customer_by_id(customer_id: int, customer: CustomerUpdateSchema,
                                session=Depends(get_async_session)) -> CustomerReadSchema:
    statement = update(Customer).where(Customer.id == customer_id).values(
        name=customer.name,
        age=customer.age,
        rating=customer.rating
    ).returning(Customer)
    result = await session.scalar(statement)
    await session.commit()
    return result

