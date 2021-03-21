from __future__ import annotations
from typing import List
from Book import Book
from datetime import date
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
        

