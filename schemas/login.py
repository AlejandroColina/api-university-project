from pydantic import UUID1, BaseModel, Field
from typing import Optional
import datetime as dt

class Login(BaseModel):
    email: str = Field(example = "abc@gmail.com")
    password: str = Field(example = "pass123")


class PersonResponse(Login):
    id: UUID1
    create_at: dt.datetime
    update_at: Optional[dt.datetime]

    class Config:
        orm_mode = True