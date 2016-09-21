"""
Test for User class
(c) Pat and Simon

Calls an object from within an object

"""

from Practical07Ext.user import User

def main():
    giver = User("Pat")
    receiver = User("Simon")

    giver.give_taco(receiver)

    print(giver)
    print(receiver)

main()