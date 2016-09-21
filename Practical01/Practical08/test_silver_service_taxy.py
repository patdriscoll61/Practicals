"""
tests the SilverServicdtaxi class
"""

from Practical08.taxi import SilverServoceTaxi

def main():
    taxi = SilverServoceTaxi("Hummer",200,4)
    print(taxi)

    taxi = SilverServoceTaxi("Mercedes",200,2)
    print(taxi)
    taxi.start_fare()
    taxi.drive(10)
    print(taxi)
    print("Fare: ${:.2f}".format(taxi.get_fare()))
main()