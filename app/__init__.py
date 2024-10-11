from fastapi import FastAPI
from database import create_db_and_tables
from config import settings
from app.api import user


    

def create_app() -> FastAPI:
    app = FastAPI(title="FastAPI Boilerplate using SQLModel")

    @app.on_event("startup")
    def on_startup():
        create_db_and_tables()

    app.include_router(user.router)

    return app





