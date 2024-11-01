from datetime import datetime
from pydantic import BaseModel


class WorkerReadSchema(BaseModel):
    id: int
    name: str
    profile: str
    age: int
    experience: int
    created_at: datetime
    updated_at: datetime

class WorkerCreateSchema(BaseModel):
    name: str
    profile: str
    age: int
    experience: int

class WorkerUpdateSchema(BaseModel):
    name: str
    profile: str
    age: int
    experience: int


