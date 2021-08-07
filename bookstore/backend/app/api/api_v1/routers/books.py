from fastapi import APIRouter, Request, Depends, Response, encoders
import typing as t

from app.db.session import get_db
from app.db.crud.book import (
    get_books,
    get_book,
    get_book_by_name,
    create_book,
    delete_book,
    edit_book,
)
from app.db.schemas.book import BookCreate, BookEdit, Book, BookOut
from app.core.auth import get_current_active_user, get_current_active_superuser

books_router = r = APIRouter()


@r.get(
    "/books",
    response_model=t.List[Book],
    response_model_exclude_none=True,
)
async def books_list(
    response: Response,
    db=Depends(get_db),
    # current_user=Depends(get_current_active_superuser),
):
    """
    Get all books
    """
    books = get_books(db)
    # This is necessary for react-admin to work
    response.headers["Content-Range"] = f"0-9/{len(books)}"
    return books

#
# @r.get("/books/me", response_model=Book, response_model_exclude_none=True)
# async def book_me(current_user=Depends(get_current_active_user)):
#     """
#     Get own book
#     """
#     return current_user


@r.get(
    "/books/{book_id}",
    response_model=Book,
    response_model_exclude_none=True,
)
async def book_details(
    request: Request,
    book_id: int,
    db=Depends(get_db),
    # current_user=Depends(get_current_active_superuser),
):
    """
    Get any book details
    """
    book = get_book(db, book_id)
    return book
    # return encoders.jsonable_encoder(
    #     book, skip_defaults=True, exclude_none=True,
    # )


@r.post("/books", response_model=Book, response_model_exclude_none=True)
async def book_create(
    request: Request,
    book: BookCreate,
    db=Depends(get_db),
    current_user=Depends(get_current_active_superuser),
):
    """
    Create a new book
    """
    return create_book(db, book)


@r.put(
    "/books/{book_id}", response_model=Book, response_model_exclude_none=True
)
async def book_edit(
    request: Request,
    book_id: int,
    book: BookEdit,
    db=Depends(get_db),
    current_user=Depends(get_current_active_superuser),
):
    """
    Update existing book
    """
    return edit_book(db, book_id, book)


@r.delete(
    "/books/{book_id}", response_model=Book, response_model_exclude_none=True
)
async def book_delete(
    request: Request,
    book_id: int,
    db=Depends(get_db),
    current_user=Depends(get_current_active_superuser),
):
    """
    Delete existing book
    """
    return delete_book(db, book_id)
