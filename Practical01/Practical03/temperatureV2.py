"""
CP1404/CP5632 - Practical
Modified from Practical01\temperature.py using refactoring for functions
"""
__author__ = 'Lindsay Ward'


def main():

    MENU = "C - Convert Celsius to Fahrenheit\nF - Convert Fahrenheit to Celsius\nQ (for quit)"
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            fahrenheit = celsius_to_farenheit()
            print("Result: {:.2f} F".format(fahrenheit))
        elif choice == "F":
            # Hint: celsius = 5 / 9 * (fahrenheit - 32)
            celsius = farenheit_to_celsius()
            print("Result: {:.2f} C".format(celsius))
            pass
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


def farenheit_to_celsius():
    farenheit = float(input("Farenheit: "))
    celsius = 5 / 9 * (farenheit - 32)
    return celsius


def celsius_to_farenheit():
    celsius = float(input("Celsius: "))
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit


main()
