from sqlalchemy import Column, ForeignKey, String, Integer
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql.expression import text
from sqlalchemy.types import DateTime
from uuid import uuid1
import datetime as dt

from db.conn import Base


class BaseModel:
    id = Column(
            UUID(as_uuid=True),
            primary_key=True,
            nullable=False,
            default=uuid1,
            comment="columna de identificatión",
        )
    created_at = Column(
            DateTime(timezone=True),
            default=dt.datetime.utcnow,
            server_default=text("NOW()"),
            nullable=False,
            comment="Timestamp de inserción",
        )
    updated_at = Column(
            DateTime(timezone=True),
            nullable=True,
            comment="TimesTamp de actualización",
            onupdate=dt.datetime.utcnow,
        )


class Person(Base, BaseModel):
    __tablename__ = "people"
    __table_args__ = ({
        "comment":"Tabla para almacenar la información de los usuarios"
    })
    name = Column(
        String,
        nullable = False,
        comment="Persiste el nombre de una persona"
    )
    last_name = Column(
        String,
        nullable = False,
        comment="Persiste el apellido de una persona"
    )


class Login(Base, BaseModel):
    __tablename__ = "login"
    __table_args__ = ({
        "comment":"Tabla para almacenar la información del login"
    })
    email = Column(
        String,
        nullable = False,
        comment="Persiste el email de una persona"
    )
    password = Column(
        String,
        nullable = False,
        comment="Persiste la contraseña de una persona"
    )