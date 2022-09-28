from typing import Any, Dict
from fastapi import HTTPException, status
from sqlalchemy import exc
from sqlalchemy.orm import Session
from pydantic import UUID1
from werkzeug.security import generate_password_hash

from schemas.person import Person



def add_resource(db: Session, resourceOne: Any, resourseTwo) -> Any:
    print("*** Adding resource ***")
    db.add(resourceOne)
    db.add(resourseTwo)
    try:
        db.commit()
        print("**** object was inserted")
        db.refresh(resourceOne)
        db.refresh(resourseTwo)
        return resourceOne
    except exc.IntegrityError as error:
        db.rollback()
        db.close()
        print("########### Error unique key ##############")
        print(error.__dict__)


def del_resource(db:Session, resource:Any) -> Any:
    print("*** Deleting person")
    db.delete(resource)
    db.commit()
    print("**** Object was deleted")
    return resource


def update_resource(db:Session, db_person:Any, body:Person):
    print("*** Updating person")
    for key, value in body.items():
        setattr(db_person, key, value)
    db.commit()
    db.refresh(db_person)
    return db_person


def encrypt_pass(login:Any)->Any:
    encrypted_login = {
        "email": login["email"],
        "password": generate_password_hash(
            login["password"],
            "pbkdf2:sha256:30",
            30
        )
    }
    return encrypted_login
    
