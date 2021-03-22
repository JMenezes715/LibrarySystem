from __future__ import annotations
from typing import List
from datetime import date
from Queue import Queue


class Book:
    """ A book in a library

    === Attributes ===
    name: the name of this book
    author: the author(s) of this book
    publication date: the publication date of this book
    wait_list: a queue of members waiting to rent the book
    """

    name: str
    author: str
    publication_date: date
    wait_list: Queue

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

        self.wait_list = Queue()
