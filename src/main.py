from fastapi import FastAPI

from admin.panel import register_admin
from database import engine
from food.router import router as food_router
from product.router import router as product_router
from worker.router import router as worker_router

app = FastAPI()
app.include_router(food_router)
app.include_router(product_router)
app.include_router(worker_router)

register_admin(app, engine)

