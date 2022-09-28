from werkzeug.security import generate_password_hash

from schemas.login import Login
from sqlalchemy.orm import Session
from typing import Optional
from pydantic import UUID1

import db.models.person as model
import services.utils as utils

# def create_person(db:Session, person:Person, login:Login):
#     login = model.Login(**login.dict())
#     return utils.add_resource(db, person, login)
