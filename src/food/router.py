from datetime import datetime

from fastapi import APIRouter, status, Depends
from sqlalchemy import insert, select, delete, update

from database import get_async_session
from .models import Food
from .schemas import FoodCreateSchema, FoodReadSchema, FoodUpdateSchema

router = APIRouter(tags=["foods"], prefix="/foods")


@router.post("/", status_code=status.HTTP_201_CREATED)  # 1) создать пищевой продукт
async def create_food(food: FoodCreateSchema, session=Depends(get_async_session)) -> FoodReadSchema:
    statement = insert(Food).values(
        name=food.name,
        price=food.price,
        expiration_date=food.expiration_date
    ).returning(Food)
    result = await session.scalar(statement)
    await session.commit()
    return result


@router.get("/", status_code=status.HTTP_200_OK)  # 2) получение данных о всех продуктах
async def get_foods(max_price: int | None = None,
                    min_price: int | None = None,
                    expiration_date: datetime | None = None,
                    session=Depends(get_async_session)) -> list[FoodReadSchema]:
    statement = select(Food)
    if max_price is not None:
        statement = statement.where(Food.price <= max_price)
    if min_price is not None:
        statement = statement.where(Food.price >= min_price)
    if expiration_date is not None:
        statement = statement.where(Food.expiration_date < expiration_date)
    result = await session.scalars(statement)
    return list(result)


@router.get("/{food_id}", status_code=status.HTTP_200_OK)  # 3) Получение данных о пищевом продукте по id
async def get_food_by_id(food_id: int, session=Depends(get_async_session)) -> FoodReadSchema:
    statement = select(Food).where(Food.id == food_id)
    result = await session.scalar(statement)
    return result


@router.delete("/{food_id}", status_code=status.HTTP_204_NO_CONTENT)  # 4) удаление пищевого продукта по id
async def delete_food_by_id(food_id: int, session=Depends(get_async_session)) -> None:
    statement = delete(Food).where(Food.id == food_id)
    await session.execute(statement)
    await session.commit()


@router.put("/{food_id}", status_code=status.HTTP_200_OK)  # 5) Обновление пищевого продукта по id
async def update_food_by_id(food_id: int, food: FoodUpdateSchema,
                            session=Depends(get_async_session)) -> FoodReadSchema:
    statement = update(Food).where(Food.id == food_id).values(
        name=food.name,
        price=food.name,
        expiration_date=food.expiration_date
    ).returning(Food)
    result = await session.scalar(statement)
    await session.commit()
    return result


