from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

USER = os.environ.get("POSTGRES_USER")
PASSWORD = os.environ.get("POSTGRES_PASSWORD")
DATABASE = os.environ.get("POSTGRES_DB")
URL = os.environ.get("POSTGRES_URL")

SQLALCHEMY_DATABASE_URL = f"postgresql://{USER}:{PASSWORD}@{URL}/{DATABASE}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()