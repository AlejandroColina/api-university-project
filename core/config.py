from pydantic import BaseSettings


credentials = {
    "dbname": "test",
    "user": "postgres",
    "host": "localhost",
    "password": "c1234567",
}

class Settings(BaseSettings):
    SQLALCHEMY_DATABASE_URL: str = f"postgresql+psycopg2://{credentials['user']}:{credentials['password']}@{credentials['host']}/{credentials['dbname']}"
    CONTAINER_NAME: str = "University project"
    VERSION: str = "0.0.1"
    PROJECT_NAME: str = "UCP-AC-DR-2022"
    DESCRIPTION: str = "Restful API - University Project"


setting = Settings()