from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

from core.config import setting

engine = create_engine(setting.SQLALCHEMY_DATABASE_URL)

Base = declarative_base()
SessionLocal = sessionmaker(bind=engine)