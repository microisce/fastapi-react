from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.db.models import Base

from app.core import config

if config.SQLALCHEMY_DATABASE_URI.split(":")[0] == "sqlite":
    print("[session] Using SQLITE for database: removing check for thread safe.")
    engine = create_engine(
        config.SQLALCHEMY_DATABASE_URI,
        pool_pre_ping=True,
        connect_args={"check_same_thread": False},
    )
else:
    engine = create_engine(
        config.SQLALCHEMY_DATABASE_URI,
    )
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base = declarative_base()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
