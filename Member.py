from __future__ import annotations
from typing import List
from Book import Book
from datetime import date, timedelta

class Member:
    """ A member that belongs to a library

    === Attributes ===
    name: the name of this member
    dob: the date of birth of this member
    rented_books: a list of books that this member is currently renting
    late_fees: the amount of money that the user owes the library
    username: the member's username for logging into the system
    password: the member's password for logging into the system

    """
    name: str
    dob: date
    rented_books: List[Book]
    late_fees: float

    username: str
    password: str

    def __init__(self, name, dob: List[str], username: str, password: str):
        self.name = name
        self.dob = date(int(dob[0]), int(dob[1]), int(dob[2]))
        self.rented_books = []
        self.late_fees = 0

        self.username = username
        self.password = password

    def __str__(self) -> str:
        return "Name: {0}, Date of Birth: {1}, Current Books Rented:" \
               "{2}".format(self.name, self.dob, len(self.rented_books))

    def __eq__(self, other: Member) -> bool:
        return self.username == other.username

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

        elif book.is_rented:
            print("The book is currently being rented and you will be placed on"
                  "the wait list.")

            book.rent_list.enqueue(self)
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
