from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from backend import models

database = "backend"
host = "localhost"
user = "backenduser"
password = "password"
port = 5432


def get_connection():
    return create_engine(
        url="postgresql://{0}:{1}@{2}:{3}/{4}".format(
            user, password, host, port, database
        )
    )

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

engine = get_connection()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
models.Base.metadata.create_all(bind=engine)