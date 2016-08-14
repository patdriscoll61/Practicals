
import random

SPECIALS = "!@#$%^&*()_-=+`~,./o'[]\<>?O{}|"
DIGITS = "0123456789"
ALPHA = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
MAX_TRIES = 1000

def main():
    # min_length = 2
    # max_length = 6
    # special_chars_required = True

    min_length = int(input(("Please enter password minimum length: ")))
    max_length = int(input("Please enter password maximum length: "))
    special_chars_required = input("Special characters required (Y/N): ").upper()
    # are_special_chars_required = True if special_chars_required == "Y" else False
    if m:
        are_special_chars_required = True
    else:
        are_special_chars_required = False

    for i in range(1,MAX_TRIES+1,1):
        password = generate_password(min_length,max_length,are_special_chars_required)
        if is_valid_password(password,min_length,max_length,are_special_chars_required):
            print("Your password is: ",password)
            break
    else:
        print("Not able to autogenerate a password in", MAX_TRIES)

def generate_password(min_length,max_length,are_special_chars_required):

    password = ""
    password_length = random.randint(min_length,max_length)
    if are_special_chars_required:
        allowable_characters = SPECIALS + DIGITS + ALPHA + ALPHA.lower()
    else:
        allowable_characters = DIGITS + ALPHA + ALPHA.lower()

    for i in range(1,password_length,1):
        password += random.choice(allowable_characters)

    return password


def is_valid_password(password,min_length,max_length,special_chars_required):
    # TODO: if length is wrong, return False
    if len(password) < min_length or len(password) > max_length:
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
        elif special_chars_required and count_special == 0:
            return False

        # if we get here (without having returned False), then the password must be valid
        return True


main()
