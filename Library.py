from __future__ import annotations
from typing import List, Dict
from Book import Book
from Member import Member


class Library:
    """ A public library containing members and books

    === Attributes ===
    name: the name of this library
    location: the location of this library
    members: the members of this library
    catalog: a list of all the books that this library owns
    available_books: a list of books that are available to rent

    """
    name: str
    location: str

    members: List[Member]
    catalog: List[Book]
    available_books: List[Book]

    def __init__(self, name: str, location: str) -> None:
        self.name = name
        self.location = location
        self.members = []
        self.books = []

    def add_member(self, member: Member) -> None:
        """ Adds a new member to the library's list of members

        :param member: The member to add to the library
        """
        if member not in self.members:
            self.members.append(member)

    def remove_member(self, member: Member) -> bool:
        """Removes this member from the library's member list.

        :param member: The member to remove from the library
        :return: True iff the member was removed. False otherwise.
        """

        for person in self.members:
            pass
