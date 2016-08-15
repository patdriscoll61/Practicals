
def main():


    #char = input("Enter a character: ")
    #print("The ASCII code for", char, "is",ord(char))
    ascii_number = get_number(10,60)
    print("The character for",ascii_number,"is",chr(ascii_number))


def get_number(lower,upper):

    valid_input = False

    while not valid_input:
        try:
            number = int(input("Enter a number (" + str(lower) + "-" + str(upper) + "): "))

            if number >= lower and number <= upper:
                valid_input = True
                return number
            else:
                print("Please enter a valid number!")
        except ValueError:
            print("Please enter a valid number!")


main()
