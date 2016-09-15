"""
Driving Simulator as per Extension WorkPracc 07
"""

from Practical07.car import Car

def main():
    print("Let's drive!")
    # name = "The bomb"
    name = input("Enter your car name: ")
    fuel = 100
    car = Car(fuel, name)
    choice = ""

    while choice != "Q":
        print("{}, fuel={}, odo={}".format(car.name, car.fuel, car.odometer, ))
        showmenu()
        choice = input("Enter your choice: ").upper()
        if choice == "D":
            ran_out_of_fuel = False
            km = int(input('How many km do you want to drive? '))
            while km < 0:
                print("Distance must be >= 0")
                km = int(input('How many km do you want to drive? '))
            if km > car.fuel:
                km = car.fuel
                ran_out_of_fuel = True
            car.drive(km)
            print("The car drove {}km {}.".format(km,"and ran out of fuel" if ran_out_of_fuel else ""))
        elif choice == "R":
            fuel_to_add = int(input("How many units of fuel do you want to add to the car? "))
            while fuel_to_add < 0:
                print("Fuel amount must be >= 0")
                fuel_to_add = int(input("How many units of fuel do you want to add to the car? "))
            car.add_fuel(fuel_to_add)
            print("Added {} units of fuel.".format(fuel_to_add))
        else:
            if choice != "Q"
                print("Invalid choice")
        print("")
    print("Good bye {}'s driver.".format(car.name))


def showmenu():
    print("Menu:")
    print("d) drive")
    print("r) refuel")
    print("q) quit")


main()