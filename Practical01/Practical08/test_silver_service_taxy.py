"""
tests the SilverServicdtaxi class
"""

from Practical08.taxi import SilverServiceTaxi

def main():
    taxi = SilverServiceTaxi("Hummer", 200, 4)
    print(taxi)

    taxi = SilverServiceTaxi("Mercedes", 200, 2)
    print(taxi)
    taxi.start_fare()
    taxi.drive(10)
    print(taxi)
    print("Fare: ${:.2f}".format(taxi.get_fare()))
main()