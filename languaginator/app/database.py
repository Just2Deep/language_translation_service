import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.config import Config


def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


engine = create_engine(Config.SQLALCHEMY_DATABASE_URI)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
