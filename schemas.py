from typing import Optional

from pydantic import BaseModel


class STaskAdd(BaseModel):
    name: str #Required
    description: Optional[str] = None #Optional not required


class STask(STaskAdd):
    id: int


class STaskId(BaseModel):
    ok: bool = True
    task_id: int