from fastapi import FastAPI

from admin.panel import register_admin
from database import engine
from food.router import router as food_router
from product.router import router as product_router
from worker.router import router as worker_router
from order.router import router as order_router
from customer.router import router as customer_router
from position.router import router as position_router

app = FastAPI()
app.include_router(food_router)
app.include_router(product_router)
app.include_router(worker_router)
app.include_router(order_router)
app.include_router(customer_router)
app.include_router(position_router)

register_admin(app, engine)

