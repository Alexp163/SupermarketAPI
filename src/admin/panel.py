from fastapi import FastAPI
from sqladmin import ModelView, Admin
from sqlalchemy.ext.asyncio import AsyncEngine

from .dependencies import Food, Product, Worker, Order


class FoodModelView(ModelView, model=Food):
    column_list = [Food.name, Food.price, Food.expiration_date]
    form_excluded_columns = [Food.created_at, Food.updated_at]


class ProductModelView(ModelView, model=Product):
    column_list = [Product.name, Product.expiration_date, Product.price, Product.balance]
    form_excluded_columns = [Product.created_at, Product.updated_at]


class WorkerModelView(ModelView, model=Worker):
    column_list = [Worker.name, Worker.profile, Worker.age, Worker.experience]
    form_excluded_columns = [Worker.created_at, Worker.updated_at]


class OrderModelView(ModelView, model=Order):
    column_list = [Order.price, Order.date_order]
    form_excluded_columns = [Order.created_at, Order.updated_at]


def register_admin(app: FastAPI, engine: AsyncEngine):
    admin = Admin(app, engine)
    admin.add_view(FoodModelView)
    admin.add_view(ProductModelView)
    admin.add_view(WorkerModelView)
    admin.add_view(OrderModelView)

