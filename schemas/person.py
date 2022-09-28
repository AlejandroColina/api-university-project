from pydantic import UUID1, BaseModel, Field
from typing import Optional
import datetime as dt


class Person(BaseModel):
    name: str = Field(example = "Alejandro")
    last_name: str = Field(example = "Colina")


class PersonResponse(Person):
    id: UUID1
    create_at: dt.datetime
    update_at: Optional[dt.datetime]

    class Config:
        orm_mode = True