"""
Test program for Guitar Class
"""

from Practical07.guitar import Guitar

def main():
    guitars = []
    # guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    # guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))
    #
    # print(guitars[0].get_age())
    # print(guitars[1].get_age())
    # print(guitars[0].is_vintage())
    # print(guitars[1].is_vintage())

    print("My guitars!")
    name = input("Name: ")
    while len(name)> 0:
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitar = guitars.append(Guitar(name,year,cost))
        print("{} added.".format(guitars[-1]))
        name = input("Name: ")
    print("These are my guitars:")
    count = 0
    for guitar in guitars:
        count += 1
        print("Guitar {}: {:>20} ({}), worth ${:10.2f} {}".format(count,guitar.name,guitar.year,guitar.cost,"(vintage)" if guitar.is_vintage() else ""))


main()


