""" Patrick Driscoll """
name = input("Enter name: ")
while not name:
    name = input("Enter name: ")
count = 0
for char in name:
    count += 1
    if count % 2 == 0:
        print(char)
