#!/usr/bin/env python3

from app.db.session import get_db
from app.db.crud.user import create_user
from app.db.crud.book import create_book
from app.db.schemas.user import UserCreate
from app.db.schemas.book import BookCreate
from app.db.session import SessionLocal


def init() -> None:
    db = SessionLocal()

    create_user(
        db,
        UserCreate(
            email="ismael@ismael.com",
            password="ismael",
            is_active=True,
            is_superuser=True,
        ),
    )
    create_book(
        db,
        BookCreate(
            name='Python For Dummies',
            author='ismael',
            image='https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/2048px-Python-logo-notext.svg.png'
        )
    )


if __name__ == "__main__":
    print("Creating superuser ismael@ismael.com")
    init()
    print("Superuser created")
