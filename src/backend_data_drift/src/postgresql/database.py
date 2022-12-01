from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
import time

USER = os.environ.get("POSTGRES_USER")
PASSWORD = os.environ.get("POSTGRES_PASSWORD")
DATABASE = os.environ.get("POSTGRES_DB")
URL = os.environ.get("POSTGRES_URL")

SQLALCHEMY_DATABASE_URL = f"postgresql://{USER}:{PASSWORD}@{URL}/{DATABASE}"

repeat = 10
is_ok = False
e_msg = None

while not is_ok and repeat != 0:
    try: 
        engine = create_engine(SQLALCHEMY_DATABASE_URL)
        SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
        Base = declarative_base()

        is_ok = True
    except Exception as e:
        e_msg = e
        time.sleep(4)
        repeat -= 1
        
if repeat == 0:
    raise RuntimeError(f"Cannot connect to Postgresql: {e_msg}")
