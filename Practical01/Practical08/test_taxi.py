"""
Tests taxi class
(c) Pat Driscoll
"""

from Practical08.taxi import Taxi

def main():
    taxi = Taxi("prius 1",100)
    print(taxi)
    taxi.drive(40)
    print(taxi)
    taxi.start_fare()
    print(taxi)
    taxi.drive(100)
    print(taxi)
    print("Fare: ${:.2f}".format(taxi.get_fare()))
main()
