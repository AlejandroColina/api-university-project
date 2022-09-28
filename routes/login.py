from fastapi import APIRouter, status, Depends
import schemas.person as schemas
from sqlalchemy.orm import Session
from typing import Optional
from pydantic import UUID1


import services.crud_people as services
from routes.dependencies import get_db


router = APIRouter()

# @router.post('/get-persons', status_code = status.HTTP_201_CREATED)
# def create_persons(
#     body: schemas.Person,
#     db: Session = Depends(get_db)
# ):
#     return services.create_person(db, body)


# @router.delete('/delete-person', status_code=status.HTTP_200_OK)
# def delete_a_person(
#     id: UUID1,
#     db: Session = Depends(get_db)
# ):
#     return services.deleting_person(db, id)


# @router.get('/search-person')
# def search_a_person(
#     db:Session = Depends(get_db),
#     id: Optional[UUID1] = None,
#     name: Optional[str] = None,
#     last_name: Optional[str] = None
# ):
#     return services.searching_a_person(
#         db=db,
#         id=id,
#         name=name,
#         last_name=last_name
#     )

# @router.patch('/update-person')
# def update_a_person(
#     body: schemas.Person,
#     id:UUID1,
#     db: Session = Depends(get_db),
# ):
#     return services.updating_a_person(db, id, body)

