"""
Guitar Class
"""

import datetime

class Guitar:
    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return "{:>25s} ({}) : $ {:<.2f}".format(self.name, self.year, self.cost)

    def get_age(self):
        age = datetime.date.today().year - self.year
        return age

    def is_vintage(self):
        return self.get_age() >= 50

    def __lt__(self,other):
        return self.year < other.year
