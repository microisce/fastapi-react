from sqlalchemy import Boolean, Column, Integer, String

from app.db.models.Base import Base


class Book(Base):
    __tablename__ = "book"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True, nullable=False)
    author = Column(String)
    image = Column(String)
