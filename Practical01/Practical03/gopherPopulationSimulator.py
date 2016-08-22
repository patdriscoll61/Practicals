"""
Gopher Population Simulator

Patrick Driscoll

"""
import random

START_POPULATION = 1000
YEARS_TO_MODEL = 10
BIRTHS_MINIMUM_PERCENT = 10    # 10 percent
BIRTHS_MAXIMUM_PERCENT = 20    # 20 percent
DEATHS_MINIMUM_PERCENT = 5     # 5 percent
DEATHS_MAXIMUM_PERCENT = 25    # 25 percent


def main():
    current_population = START_POPULATION
    print("Welcome to the Gopher Population Simulator!")
    print("Starting Population: {}".format(START_POPULATION))
    for i in range(1,YEARS_TO_MODEL+1):
        births = round(current_population * random.randint(BIRTHS_MINIMUM_PERCENT,BIRTHS_MAXIMUM_PERCENT)/100)
        deaths =  round(current_population * random.randint(DEATHS_MINIMUM_PERCENT,DEATHS_MAXIMUM_PERCENT)/100)
        current_population = current_population + births - deaths
        print("Year {}".format(i))
        print("*****")
        print("{} gophers were born. {} died.".format(births,deaths))
        print("Population: {}".format(current_population))


main()
