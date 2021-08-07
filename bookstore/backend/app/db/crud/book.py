from fastapi import HTTPException, status
from sqlalchemy.orm import Session
import typing as t

from app.db.models import book as models
from app.db.schemas import book as schemas


def get_book(db: Session, book_id: int):
    book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book


def get_book_by_name(db: Session, name: str) -> schemas.BookBase:
    return db.query(models.Book).filter(models.Book.name == name).first()


def get_books(
    db: Session, skip: int = 0, limit: int = 100
) -> t.List[schemas.BookOut]:
    return db.query(models.Book).offset(skip).limit(limit).all()


def create_book(db: Session, book: schemas.BookCreate):

    db_book = models.Book(
        name=book.name,
        author=book.author,
        image=book.image,
    )
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book


def delete_book(db: Session, book_id: int):
    book = get_book(db, book_id)
    if not book:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="Book not found")
    db.delete(book)
    db.commit()
    return book


def edit_book(
    db: Session, book_id: int, book: schemas.BookEdit
) -> schemas.Book:
    db_book = get_book(db, book_id)
    if not db_book:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="Book not found")
    update_data = book.dict(exclude_unset=True)

    for key, value in update_data.items():
        setattr(db_book, key, value)

    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book
