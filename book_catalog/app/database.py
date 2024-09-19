from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

SQLALCHEMY_DATABASE_URL = "postgresql://db_722task7p2_user:i6IXzaM7YCtr6UC8GXhLIVBvfkWuSnxC@dpg-crhvjsjtq21c738477ag-a.oregon-postgres.render.com/db_722task7p2" #os.getenv("DATABASE_URL")

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
