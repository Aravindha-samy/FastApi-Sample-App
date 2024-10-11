from config import settings
from sqlmodel import create_engine,Session,SQLModel

engine = create_engine(settings.postgres_url, echo=True)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)
    print("Database connected successfully")

def get_session():
    """Dependency to get a new SQLModel session"""
    with Session(engine) as session:
        yield session
    

