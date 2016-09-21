"""
Tests Unreliable Car Class
"""

import random
from Practical08.taxi import UnreliableCar

def main():
    bomb = UnreliableCar("Lada",120,65)
    print(bomb)
    bomb.drive(20)
    print(bomb)


main()