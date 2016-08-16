"""
CP1404/CP5632 - Practical
Random word generator - based on format of words

(Another way to get just consonants would be to use string.ascii_lowercase (all letters) and remove the vowels)
"""
import random

VOWELS = "aeiou"
CONSONANTS = "bcdfghjklmnpqrstvwxyz"
EXIT_CHAR = "!"
RANDOM_FLAG = "#ran"

def main():
    word_format = "ccvcvvc"
    is_entry_ok = False

    while word_format != EXIT_CHAR:
        word_format = input("Enter word format (% = consontant, # = vowel, * = wildcard, "+ EXIT_CHAR +" to Exit), " + RANDOM_FLAG + " for Random: ").lower()
        if word_format == RANDOM_FLAG:
            word_format = ""
            word_format_length = int(random.choice("345678"))
            for i in range(1,word_format_length+1):
                word_format += random.choice(CONSONANTS+VOWELS+"%#*")
        while not is_entry_ok:
            is_entry_ok = check_entry(word_format)
            if not is_entry_ok:
                word_format = input("Enter word format (% = consontant, # = vowel ! to Exit): ").lower()
        if EXIT_CHAR not in word_format:
            word = ""
            for kind in word_format:
                if kind == "#": # Vowels
                    word += random.choice(CONSONANTS)
                elif kind == "%":   # Consonants
                    word += random.choice(VOWELS)
                elif kind == "*":    # Vowels or Consonants
                    word += random.choice(CONSONANTS + VOWELS)
                else:
                    word += kind
            print(word)

def check_entry(word_format):
    for char in word_format:
        if char not in "#%*!" + CONSONANTS + VOWELS:
            print("Invalid Entry")
            return False
    return True

main()