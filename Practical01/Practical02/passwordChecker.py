"""
CP1404/CP5632 - Practical
Password checker "skeleton" code to help you get started
"""

MIN_LENGTH = 2
MAX_LENGTH = 6
SPECIAL_CHARS_REQUIRED = True
SPECIALS = "!@#$%^&*()_-=+`~,./o'[]\<>?O{}|"


def main():
    print("Please enter a valid password")
    print("Your password must be between", MIN_LENGTH, "and", MAX_LENGTH, "characters, and contain:")
    print("\t1 or more uppercase characters")
    print("\t1 or more lowercase characters")
    print("\t1 or more numbers")
    if SPECIAL_CHARS_REQUIRED:
        print("\tand 1 or more special characters: ", SPECIALS)
    password = input("> ")
    while not is_valid_password(password):
        print("Invalid password!")
        password = input("> ")
    print("Your " + str(len(password)) + " character password is valid: " + password)


def is_valid_password(password):
    # TODO: if length is wrong, return False
    if len(password) < MIN_LENGTH or len(password) > MAX_LENGTH:
        return False
    else:
        count_lower = 0
        count_upper = 0
        count_digit = 0
        count_special = 0
        for char in password:
            # TODO: count each kind of character
            if char.islower():
                count_lower += 1
            elif char.isupper():
                count_upper += 1
            elif char in "0123456789":
                count_digit += 1
            elif char in SPECIALS:
                count_special += 1

        # TODO: if any of the 'normal' counts are zero, return False
        if count_lower == 0 or count_upper == 0 or count_digit == 0:
            return False
        # TODO: if special characters are required, then check the count of those and return False if it's zero
        elif SPECIAL_CHARS_REQUIRED and count_special == 0:
            return False

        # if we get here (without having returned False), then the password must be valid
        return True


main()

