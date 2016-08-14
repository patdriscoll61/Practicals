number_file = open("numbers.txt","r")
number1 = int(number_file.readline().strip())
number2 = int(number_file.readline().strip())
total = number1 + number2
print(total)
number_file.close()

