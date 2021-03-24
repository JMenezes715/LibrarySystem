from __future__ import annotations
from Library import *
from Member import *
from Book import *

if __name__ == '__main__':

    Central_Library = Library("Central Library", "123 Fake Address")

    The_Hunger_Games = Book("The Hunger Games", "Suzanne Collins",
                            [2008, 9, 14])

    The_Lightning_Thief = Book("The Lightning Thief", "Rick Riordan",
                               [2005, 6, 28])

    print(The_Hunger_Games)
    print(The_Lightning_Thief)

    Central_Library.add_book(The_Hunger_Games)
    Central_Library.add_book(The_Lightning_Thief)

    name = input("Enter your full name: ")
    dob_year = "Enter the year you were born: "
    dob_month = "Enter the month you were born: "
    dob_day = "Enter the day you were born: "
    user_name = input("Enter a username: ")
    password = input("Enter a password: ")

    test_member = Member(name, [dob_year, dob_month, dob_day], user_name,
                         password)

    print(test_member)

    Central_Library.add_member(test_member)
