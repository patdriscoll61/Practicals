"""
CP1404/CP5632 Practical
File and class example - opens/reads a file, stores in objects of custom class
(contains multiple versions for demonstration: using csv and namedtuple)
"""

def main():
    """ read a file of guitar details, save as objects, display """
    guitars = []
    in_file = open('guitars.csv', 'r')
    for line in in_file:
        guitar = tuple(line.strip().split(","))
        guitars.append(guitar)
    in_file.close()

    for guitar in guitars:
        print(guitar)


main()