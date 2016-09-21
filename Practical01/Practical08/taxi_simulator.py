"""
Taxi Simulator using Taxi and SilverService taxi classes
"""

from Practical08.taxi import Taxi
from Practical08.taxi import SilverServiceTaxi


def main():
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    total_bill = 0

    print("Let's drive!")
    choice = ""
    while choice != "Q":
        print("q)uit. c)hoose taxi, d)rive")
        choice = input(">>>").upper()
        if choice == "C":
            print("Taxis available:")
            print("0 - {}".format(taxis[0]))
            print("1 - {}".format(taxis[1]))
            print("2 - {}".format(taxis[2]))
            valid_input = False
            while not valid_input:
                try:
                    taxi_choice = int(input("Choose taxi: "))
                    if taxi_choice == 0 or taxi_choice == 1 or taxi_choice == 2:
                        taxi = taxis[taxi_choice]
                        valid_input = True
                    else:
                        print("Invalid Taxi Choice")

                except ValueError:
                    print("Please Enter a Valid Taxi Choice")

        elif choice == "D":
            distance = int(input("Drive how far? "))
            taxi.start_fare()
            taxi.drive(distance)
            total_bill += taxi.get_fare()
            print("Your {} trip cost you ${:.2f}".format(taxi.name, taxi.get_fare()))
        elif choice != "Q":
            print("Invalid Option")

        print("Bill to date: ${:.2f}".format(total_bill))


main()
