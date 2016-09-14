"""
CP1404/CP5632 Practical
Client code to use the Car class
Note that the import has a folder (module) in it.
"""
from Practical07.car import Car


def main():
    bus = Car(180)
    bus.drive(30)
    print("fuel =", bus.fuel)
    print("odo =", bus.odometer)
    print(bus)

    print("Car {}, {}".format(bus.fuel, bus.odometer))
    print("Car {self.fuel}, {self.odometer}".format(self=bus))

    print("limo:")
    limo = Car(100,name="limo")
    limo.add_fuel(20)
    print("fuel =",limo.fuel)
    limo.drive(115)
    print("odo =", limo.odometer)
    print(limo)

main()