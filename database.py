from sqlmodel import create_engine, SQLModel, Session
from typing import Annotated
from fastapi import Depends

DB_URL = "sqlite:///./products.db"

engine = create_engine(
    DB_URL,
    connect_args={"check_same_thread": False}
)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

# Session management principles:
# Request received 
# => opens a DB session  
# => processes request while communicating with the DB
# => response sent 
# => closes the session

def get_session():
    with Session(engine) as session:
        yield session

SessionDep = Annotated[Session, Depends(get_session)]