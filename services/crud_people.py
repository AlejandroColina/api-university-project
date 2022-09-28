from schemas.person import Person
from schemas.login import Login
from sqlalchemy.orm import Session
from typing import Optional
from pydantic import UUID1


import db.models.person as model
import services.utils as utils


def create_person(db:Session, person:Person, login:Login):
    new_login= utils.encrypt_pass(login.dict())
    person = model.Person(**person.dict())
    login = model.Login(**new_login)
    return utils.add_resource(db, person, login)


def deleting_person(db:Session, id:UUID1)-> model.Person:
    person = db.query(model.Person).filter(model.Person.id == id).first()
    if person is None:
        return person
    else:
        return utils.del_resource(db, person)


def searching_a_person(
    db:Session,
    id: Optional[UUID1] = None,
    name: Optional[str] = None,
    last_name: Optional[str] = None
)-> model.Person:
    person = db.query(model.Person)
    print("Searching person")

    if id:
        person = person.filter(model.Person.id == id).first()
        return person

    if name:
        person = person.filter(model.Person.name == name).first()
        return person

    if last_name:
        person = person.filter(model.Person.last_name == last_name).first()
        return person

    return person.all()


def updating_a_person(db:Session,id:UUID1, body:Person):
    db_person = db.query(model.Person).filter(model.Person.id == id).first()
    if db_person is None:
        return db_person
    else:
        return utils.update_resource(
            db, 
            db_person,
            body=body.dict(exclude_unset=True)
        )
    
