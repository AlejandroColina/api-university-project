from fastapi import APIRouter
import routes.person as person
import routes.login as login


api_router = APIRouter()
api_router.include_router(person.router, prefix='/person', tags=["People"])
api_router.include_router(login.router, prefix='/login', tags=["Login"])
