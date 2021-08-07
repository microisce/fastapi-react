from pydantic import BaseModel
# import typing as t


class BookBase(BaseModel):
    name: str
    image: str
    author: str


class BookOut(BookBase):
    pass


class BookCreate(BookBase):

    class Config:
        orm_mode = True


class BookEdit(BookBase):

    class Config:
        orm_mode = True


class Book(BookBase):
    id: int

    class Config:
        orm_mode = True

