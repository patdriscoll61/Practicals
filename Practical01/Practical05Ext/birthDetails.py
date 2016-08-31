
import datetime

def main1():
    birthday_dict = {}
    for i in range(1,6):
        name = input("Enter Name: ")
        birth_date = input(("Enter Birth Date (DD/MM/YYYY)"))
        birthday_dict[name] = birth_date.split("/")
    print(birthday_dict)
    #birthday_dict = {'Pat': ['17', '02', '1961'], 'Lisa': ['09', '05', '1989'], 'Kerry': ['11', '08', '1965'], 'Jymii': ['15', '07', '1982'], 'Rebecca': ['21', '07', '1991']}
    for name in birthday_dict:
         print("{} is {} this year.".format(name, datetime.date.today().year - int(birthday_dict[name][2])))

main()