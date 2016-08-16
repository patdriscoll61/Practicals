"""
CP1404/CP5632 - Practical
Fixed program to determine score status
Modified using refactoring to make a function
"""

def main():
    score = get_score()
    print(score_to_result(score))


def score_to_result(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score > 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"

def get_score():
    valid_input = False
    while not valid_input:
        try:
            entered_score = int(input("Enter score: "))
            valid_input = True
            return entered_score
        except ValueError:
            print("Please enter a valid number!")

main()
