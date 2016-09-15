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
        return "{:>20s} ({}) : $ {:<.2f}".format(self.name, self.year, self.cost)

    def get_age(self):
        age = datetime.date.today().year - self.year
        return age

    def is_vintage(self):
        age = datetime.date.today().year - self.year
        return True if age >= 50 else False