""" Patrick Driscoll """
def main():

    name = get_name()
    print(name[1:len(name):3])


def get_name():
    name = input("Enter name: ")
    while not name:
        name = input("Enter name: ")
    return name


main()
