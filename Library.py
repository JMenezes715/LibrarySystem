from __future__ import annotations
from typing import List, Dict


class Library:
    """ A public library containing members and books

    === Attributes ===
    name: the name of this library
    location: the location of this library
    members: the members of this library
    books: the current books that this library has

    """
    name: str
    location: str

    members: List[object]
    books: List[object]
    # TODO object placeholders for member and book class

    def __init__(self, name: str, location: str) -> None:
        self.name = name
        self.location = location
        self.members = []
        self.books = []

    def add_member(self, member: object) -> None:
        """ Adds a new member to the library's list of members

        :param member:
        :return:
        """
        if member not in self.members:
            self.members.append(member)

    def remove_member(self, member: object) -> bool:
