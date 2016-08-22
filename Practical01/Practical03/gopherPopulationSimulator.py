"""
Gopher Population Simulator

Patrick Driscoll

"""
import random

START_POPULATION = 1000
YEARS_TO_MODEL = 10
BIRTHS_MINIMUM_PERCENT = 10
BIRTHS_MAXIMUM_PERCENT = 20
DEATHS_MINIMUM_PERCENT = 5
DEATHS_MAXIMUM_PERCENT = 25


def main():
    current_population = START_POPULATION
    print("Welcome to the Gopher Population Simulator!","Starting Population: " + str(START_POPULATION))
    for i in range(1,YEARS_TO_MODEL+1):
        births = current_population * random.randint(BIRTHS_MINIMUM_PERCENT,BIRTHS_MAXIMUM_PERCENT)
        deaths =  current_population * random.randint(DEATHS_MINIMUM_PERCENT,DEATHS_MAXIMUM_PERCENT)
        current_population = current_population + births - deaths
        print("Year " + i.string(),"*****")
        print("{} gophers were born. {} died.".format(births,deaths))
main()
