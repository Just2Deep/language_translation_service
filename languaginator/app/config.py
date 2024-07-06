""" Configuration Data for the database"""

from os import getenv
from dotenv import load_dotenv

load_dotenv()

USER_NAME = getenv("USER_NAME")
PASSWORD = getenv("PASSWORD")
HOSTNAME = getenv("HOSTNAME")
DBNAME = getenv("DBNAME")
OPENAI_API_KEY = getenv("OPENAI_API_KEY")


class Config:
    DEBUG = True

    SQLALCHEMY_DATABASE_URI = (
        f"postgresql+psycopg2://{USER_NAME}:{PASSWORD}@{HOSTNAME}/{DBNAME}"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    OPENAI_API_KEY = OPENAI_API_KEY
