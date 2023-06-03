from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database

SQLALCHEMY_DATABASE_URL = "postgresql://dev_user:dev_password@db:5432/user_db"
if not database_exists(SQLALCHEMY_DATABASE_URL):
    create_database(SQLALCHEMY_DATABASE_URL)

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    pool_size=50
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
