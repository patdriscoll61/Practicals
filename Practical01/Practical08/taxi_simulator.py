"""
Taxi Simulator using Taxi and SilverService taxi classes
"""

from Practical08.taxi import Taxi
from Practical08.taxi import SilverServiceTaxi


def main():

    MENU = "q)uit. c)hoose taxi, d)rive"
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    total_bill = 0

    print("Let's drive!")
    # TODO Use a trailing else and ask choice twice
    print(MENU)  # TODO make a constant
    choice = input(">>>").upper()
    while choice != "Q":
        if choice == "C":
            # TODO Use for taxi in taxis
            print("Taxis available:")
            nCount = 0
            for taxi in taxis:
                print("{} - {}".format(nCount,taxis[0]))
                nCount += 1
            valid_input = False
            while not valid_input:
                try:
                    taxi_choice = int(input("Choose taxi: "))
                    # TODO Fix this for any number of taxis
                    if taxi_choice >= 0 and taxi_choice <= nCount - 1:
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
        else:
            print("Invalid Option")

        print("Bill to date: ${:.2f}".format(total_bill))
        print(MENU)  # TODO make a constant
        choice = input(">>>").upper()

main()
