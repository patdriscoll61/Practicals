number_file = open("numbers.txt","r")
total = 0
for number in number_file:
    number = int(number.strip())
    total += number
print("Total is:",total)
number_file.close()