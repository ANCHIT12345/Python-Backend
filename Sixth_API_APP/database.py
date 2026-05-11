from sqlalchemy import create_engine  # type: ignore[import-not-found]
from sqlalchemy.orm import sessionmaker, declarative_base  # type: ignore[import-not-found]

DATABASE_URL = ("mssql+pyodbc://username:password@localhost/HospitalManagementSystem?driver=ODBC+Driver+17+for+SQL+Server")

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)   

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()