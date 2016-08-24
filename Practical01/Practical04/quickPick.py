"""
Lotto Quick Pick Generator
"""

import random

def main():
    games = int(input("How many quick picks? "))
    for i in range(games):
        quick_picks = []
        while len(quick_picks) < 6:
            number = random.randint(1,45)
            if number not in quick_picks:
                quick_picks.append(number)
        quick_picks.sort()
        for j in range(len(quick_picks)):
            print("{:2d}".format(quick_picks[j]), end=" ")
        print("\r")
main()