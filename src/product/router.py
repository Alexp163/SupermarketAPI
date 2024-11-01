from fastapi import APIRouter, status, Depends
from sqlalchemy import insert, select, delete, update
from .models import Product
from .schemas import ProductCreateSchema, ProductReadSchema, ProductUpdateSchema

from database import get_async_session



router = APIRouter(tags=['product'], prefix="/product")

@router.post("/", status_code=status.HTTP_201_CREATED)  # 1) Создание данных о продукте
async def create_product(product: ProductCreateSchema, session=Depends(get_async_session)) -> ProductReadSchema:
    statement = insert(Product).values(
        name=product.name,
        expiration_date=product.expiration_date,
        price=product.price,
        balance=product.balance
    ).returning(Product)
    result = await session.scakar(statement)
    await session.commit()
    return result


@router.get("/", status_code=status.HTTP_200_OK)  # 2) Получение данных о всех продуктах
async def get_products(session=Depends(get_async_session)) -> list[ProductReadSchema]:
    statement = select(Product)
    result = await session.scalars(statement)
    return list(result)


@router.get("/{product_id}", status_code=status.HTTP_200_OK)  # 3) Получение данных о продукте по id
async def get_product_by_id(product_id: int, session=Depends(get_async_session)) -> ProductReadSchema:
    statement = select(Product).where(Product.id == product_id)
    result = await session.scalar(statement)
    return result


@router.delete("/{product_id}", status_code=status.HTTP_200_OK)  # 4) Удаление данных о продукте по id
async def delete_product_by_id(product_id: int, session=Depends(get_async_session)) -> None:
    statement = delete(Product).where(Product.id == product_id)
    await session.execute(statement)
    await session.commit()


@router.put("/product_id", status_code=status.HTTP_200_OK)  # 5) Обновление данных о продукте
async def update_product_by_id(product_id: int, product: ProductUpdateSchema,
                               session=Depends(get_async_session)) -> ProductReadSchema:
    statement = update(Product).where(Product.id == product_id).values(
        name=product.name,
        expiration_date=product.expiration_date,
        price=product.price,
        balance=product.balance
    ).returning(Product)
    result = await session.scalar(statement)
    return result



