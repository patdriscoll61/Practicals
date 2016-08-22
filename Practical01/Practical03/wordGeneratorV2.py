"""
CP1404/CP5632 - Practical
Random word generator - based on format of words

(Another way to get just consonants would be to use string.ascii_lowercase (all letters) and remove the vowels)
"""
import random

VOWELS = "aeiou"
CONSONANTS = "bcdfghjklmnpqrstvwxyz"
EXIT_CHAR = "!"


def main():
    word_format = "ccvcvvc"

    while word_format != EXIT_CHAR:
        is_entry_ok = False
        while not is_entry_ok:
            word_format = input("Enter word format c = consontant, v = vowel (" + EXIT_CHAR + " to Exit): ").lower()
            is_entry_ok = is_valid_format(word_format)
        if EXIT_CHAR not in word_format:
            word = ""
            for kind in word_format:
                if kind == "c": # Vowels
                    word += random.choice(CONSONANTS)
                elif kind == "v":   # Consonants
                    word += random.choice(VOWELS)
            print(word)


def is_valid_format(word_format):
    for char in word_format:
        if char not in "cv!":
            return False
    return True


main()