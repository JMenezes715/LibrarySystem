from __future__ import annotations
from typing import List
from datetime import date, timedelta
from Queue import Queue
from Member import Member


class Book:
    """ A book in a library

    === Attributes ===
    name: the name of this book
    author: the author(s) of this book
    publication date: the publication date of this book
    wait_list: a queue of members waiting to rent the book
    due_date: the date that this book must be returned
    is_rented: the status of the book regarding renting it

    * Note that the member at the front of the queue represents the user who is
    currently holding the book *

    === Representation Invariants ===
    is_rented = False => Book.rent_list.is_empty() = True
    """

    name: str
    author: str
    publication_date: date
    rent_list: Queue
    due_date: date
    is_rented: bool

    def __init__(self, name: str, author: str, publication_date: List[int]):
        """ Creates a new Book object

        :param name: the name of the book
        :param author: the author of the book
        :param publication_date: a list containing the year, month, and date of
        publication
        """
        self.name = name
        self.author = author
        self.publication_date = date(int(publication_date[0]),
                                     int(publication_date[1]),
                                     int(publication_date[2]))

        self.rent_list = Queue()
        self.due_date = date.today()
        self.is_rented = False

    def __str__(self):
        return "{0}, by {1}".format(self.name, self.author)

    def __eq__(self, other: Book):
        return self.name == other.name and self.author == other.author

    def is_available(self) -> bool:
        """ Returns true iff this book is available to rent. False otherwise
        """

        return self.rent_list.is_empty()
