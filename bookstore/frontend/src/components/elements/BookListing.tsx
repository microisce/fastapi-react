import React from 'react'
import {Book} from "./Book";
import {IBook} from "../../shared/interfaces";

interface IProps{
    books: IBook[]
}
export function BookListing(props: IProps) {
    const books = props.books
    return(
        <div className={'listing'} >
            {
                books.map(book =>
                    <Book  author={book.author} image={book.image} name={book.name}/>
                )
            }
        </div>
    )
}
