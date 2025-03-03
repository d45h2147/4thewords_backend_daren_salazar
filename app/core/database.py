from sqlmodel import SQLModel, create_engine, Session
from sqlmodel import SQLModel, create_engine

from app.core.settings import app_setting


engine = create_engine(app_setting.db_uri, echo=True)


def get_session():
    with Session(engine) as session:
        yield session


def init_db():
    SQLModel.metadata.create_all(engine)
