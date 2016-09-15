"""
Driving Simulator as per Extension WorkPracc 07
"""

from Practical07.car import Car

def main():
    # name = input("Enter you car name: ")
    name = "The bomb"
    fuel = 100
    car = Car(fuel,name)
    print("{}, fuel={}, odo={}".format(car.name,car.fuel,car.odometer,))

    km = int(input('How many km do you want to drive? '))
    while km < 0:
        print("Distance must be >= 0")
        km = int(input('How many km do you want to drive? '))
    car.drive(km)
    print("The car drove {}km".format(km))

    fuel_to_add = int(input("How many units of fuel do you want to add to the car? "))
    while fuel_to_add < 0:
        print("Fuel amount must be >= 0")
        fuel_to_add = int(input("How many units of fuel do you want to add to the car? "))
    car.fuel(fuel_to_add)
    print("Added {} units of fuel.".format(fuel_to_add))

def


main()