from __future__ import annotations
from typing import List
from Book import Book
from datetime import date, timedelta
from uuid import uuid4


class Member:
    """ A member that belongs to a library

    === Attributes ===
    name: the name of this member
    member_id: the 7 digit id of this member
    dob: the date of birth of this member
    rented_books: a list of books that this member is currently renting


    """
    name: str
    member_id: int
    dob: date
    rented_books: List[Book]

    def __init__(self, name, dob: List[str]):
        self.name = name
        self.member_id = uuid4().int
        # Generate a random uuid number in a 128 bit representation
        self.dob = date(int(dob[0]), int(dob[1]), int(dob[2]))
        self.rented_books = []

    def __str__(self) -> str:
        return "Name: {0}, ID: {1}, Date of Birth: {2}, Current Books Rented:" \
               "{3}".format(self.name, self.member_id, self.dob,
                            len(self.rented_books))

    def __eq__(self, other: Member) -> bool:
        return self.member_id == other.member_id

    def rent_book(self, book: Book) -> bool:
        """ Rents this book

        :param book: The book to be rented
        :return: True iff the book was successfully rented. False otherwise
        """

        if not book.is_rented and book not in self.rented_books:
            book.due_date = date.today() + timedelta(days=7)
            book.is_rented = True
            book.rent_list.enqueue(self)
            # Add the member to the front of the queue to signify that they
            # are renting the book

            self.rented_books.append(book)

            return True
        return False

    def renew_book(self, book) -> bool:
        """ Renews this book for one week

        :param book: The book to be renewed
        :return: True iff the book was successfully renewed. False otherwise
        """

        if book in self.rented_books:
            book.due_date = date.today() + timedelta(days=7)
            return True

        return False

    def return_book(self, book) -> bool:
        """ Returns this book to the library

        :param book: The book to be returned
        :return: True iff the book was successfully returned. False otherwise
        """

        if book in self.rented_books:
            book.is_rented = False
            book.rent_list.dequeue()
            # Remove them from the renting list

            self.rented_books.remove(book)
            # Remove the book from the user's rented books

            return True
        return False
