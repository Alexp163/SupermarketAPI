from fastapi import APIRouter, Depends, status
from sqlalchemy import select, insert, delete, update
from database import get_async_session
from .models import Worker
from .schemas import WorkerCreateSchema, WorkerReadSchema, WorkerUpdateSchema

router = APIRouter(tags=["workers"], prefix="/workers")


@router.post("/", status_code=status.HTTP_201_CREATED)  # 1) создание данных о новом рабочем
async def create_worker(worker: WorkerCreateSchema, session=Depends(get_async_session)) -> WorkerReadSchema:
    statement = insert(Worker).values(
        name=worker.name,
        pfrofile=worker.profile,
        age=worker.age,
        experience=worker.experience
    ).returning(Worker)
    result = await session.scalar(statement)
    await session.commit()
    return result


@router.get("/", status_code=status.HTTP_200_OK)  # 2) вывести данные о всех рабочих
async def get_workers(max_age: int | None = None,
                      min_age: int | None = None,
                      max_experience: int | None = None,
                      min_experience: int | None = None,
                      session=Depends(get_async_session)) -> list[WorkerReadSchema]:
    statement = select(Worker)
    if max_age is not None:
        statement = statement.where(Worker.age <= max_age)
    if min_age is not None:
        statement = statement.where(Worker.age >= min_age)
    if max_experience is not None:
        statement = statement.where(Worker.experience <= max_experience)
    if min_experience is not None:
        statement = statement.where(Worker.experience >= min_experience)
    result = await session.scalars(statement)
    return list(result)


@router.get("/{worker_id}", status_code=status.HTTP_200_OK)  # 3) вывести о рабочем по id
async def get_worker_by_id(worker_id: int, session=Depends(get_async_session)) -> WorkerReadSchema:
    statement = select(Worker).where(Worker.id == worker_id)
    result = await session.scalar(statement)
    return result


@router.delete("/{worker_id}", status_code=status.HTTP_204_NO_CONTENT)  # 4) удалить данные о рабочем по id
async def delete_worker_by_id(worker_id: int, session=Depends(get_async_session)) -> None:
    statement = delete(Worker).where(Worker.id == worker_id)
    await session.execute(statement)
    await session.commit()


@router.put("/{worker_id}", status_code=status.HTTP_200_OK)  # 5) обновить данные о рабочем по id
async def upgrade_worker_by_id(worker_id: int, worker: WorkerUpdateSchema,
                               session=Depends(get_async_session)) -> WorkerReadSchema:
    statement = update(Worker).where(Worker.id == worker_id).values(
        name=worker.name,
        pfrofile=worker.profile,
        age=worker.age,
        experience=worker.experience
    ).returning(Worker)
    result = await session.scalar(statement)
    await session.commit()
    return result
