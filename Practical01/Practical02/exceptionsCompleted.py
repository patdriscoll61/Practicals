"""
CP1404/CP5632 - Practical
Fill in the TODOs to complete the task
"""

finished = False
result = 0
while not finished:
    try:
        result = int(input("Enter an Integer: "))
        finished = True
    except ValueError:  # TODO - add something after except
        print("Please enter a valid integer.")
print("Valid result is:", result)