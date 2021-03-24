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
    book_list: a list of all the books that this library owns

    """
    name: str
    location: str
    members: List[Member]
    book_list: List[Book]

    def __init__(self, name: str, location: str) -> None:
        self.name = name
        self.location = location
        self.members = []
        self.book_list = []

    def add_book(self, book: Book) -> bool:
        """ Adds book to the library's book list

        :param book: The book to be added to the library
        :return: True if this book was successfully added to the library's
        book list. False otherwise
        """

        if book not in self.book_list:
            self.book_list.append(book)
            book.owned_by = self
            return True

        print("This book is already in the library's book list!")
        return False

    def remove_book(self, book: Book) -> bool:
        """ Removes book from the library's book list

        :param book: The book to be removed from the library
        :return: True if the book was successfully removed from the library's
        book list. False otherwise
        """

        try:
            self.book_list.remove(book)

        except ValueError:
            print("Book not found. Try again.")
            return False

        return True

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

        try:
            self.members.remove(member)

        except ValueError:
            print("Member does not exist. Please try again.")
            return False

        return True
