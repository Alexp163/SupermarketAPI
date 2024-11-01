from fastapi import APIRouter, status, Depends
from sqlalchemy import insert, select, delete, update

from database import get_async_session
from .models import Order
from .schemas import OrderReadSchema, OrderUpdateSchema, OrderCreateSchema


router = APIRouter(tags=["orders"], prefix="/orders")

@router.post("/", status_code=status.HTTP_201_CREATED)  # 1) создание заказа
async def create_order(order: OrderCreateSchema, session=Depends(get_async_session)) -> OrderReadSchema:
    statement = insert(Order).values(
        price=order.price,
        date_order=order.date_order
    ).returning(Order)
    result = await session.scalar(statement)
    return result


@router.get("/", status_code=status.HTTP_200_OK)  # 2) получить данные о всех заказах
async def get_orders(session=Depends(get_async_session)) -> list[OrderReadSchema]:
    statement = select(Order)
    result = await session.scalars(statement)
    return result


@router.get("/{order_id}", status_code=status.HTTP_200_OK)  # 3) получить данные о заказе по id
async def get_order_by_id(order_id: int, session=Depends(get_async_session)) -> OrderReadSchema:
    statement = select(Order).where(Order.id == order_id)
    result = await session.scalar(statement)
    return result


@router.delete("/{order_id}", status_code=status.HTTP_204_NO_CONTENT)  # 4) удалить данные о заказе по id
async def delete_order_by_id(order_id: int, session=Depends(get_async_session)) -> None:
    statement = delete(Order).where(Order.id == order_id)
    await session.execute(statement)
    await session.commit()


@router.put("/{order_id}", status_code=status.HTTP_200_OK)  # 5) обновить данные о заказе по id
async def update_order_by_id(order_id: int, order: OrderUpdateSchema,
                             session=Depends(get_async_session)) -> OrderReadSchema:
    statement = update(Order).where(Order.id == order_id).values(
        price=order.price,
        date_order=order.date_order
    ).returning(Order)
    result = await session.scalar(statement)
    await session.commit()
    return result

