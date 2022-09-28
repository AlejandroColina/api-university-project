from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes.router import api_router
from core.config import setting
from db.conn import Base, engine

def run_application () -> FastAPI:
    excecution = FastAPI(
        title = setting.CONTAINER_NAME,
        version = setting.VERSION,
        description = setting.DESCRIPTION,
    )

    excecution.add_middleware(CORSMiddleware, allow_origins=["*"])
    excecution.include_router(api_router)

    return excecution

app = run_application()
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)