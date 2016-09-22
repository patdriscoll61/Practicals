"""
CP1404/CP5632 Practical
File and class example - opens/reads a file, stores in objects of custom class
(contains multiple versions for demonstration: using csv and namedtuple)
"""

import csv
from collections import namedtuple
from Practical08Ext.guitar import Guitar

def main():
    """ read a file of guitar details, save as objects, display """
    guitars = []
    in_file = open('myguitars.csv', 'r')
    for line in in_file:
        guitar_data = tuple(line.strip().split(","))
        guitar = Guitar(guitar_data[0], guitar_data[1], float(guitar_data[2]))
        guitars.append(guitar)

    in_file.close()

    for guitar in guitars:
        print(guitar)

    guitars.sort()

    print("Sorted by year:")
    for guitar in guitars:
        print(guitar)

    # out_file = open('myguitars.csv',"+w")
    # for guitar in guitars:
    #     print("{}, {}, {:.2f}".format(guitar.name, guitar.year, guitar.cost), file=out_file)
    # out_file.close()




main()