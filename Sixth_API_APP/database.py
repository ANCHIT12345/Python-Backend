from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

DATABASE_URL = ("mssql+pyodbc://username:password@localhost/hospital_db?driver=ODBC+Driver+17+for+SQL+Server")

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)   

Base = declarative_base()

