
x = int(input("Enter in Start Number: "))
y = int(input("Enter in Finish Number: "))

choice = 1

while choice == 1 or choice == 2 or choice == 3:

    print("1. Show the even numbers from x to y")
    print("2. Show the odd numbers from x to y")
    print("3. Show the squares from x to y")
    print("4. Exit the Program")

    choice = int(input("Enter Menu Choice:"))

    if choice == 1:
        if x%2 == 0:
            for i in range(x,y+1,2):
                print(i,end = " ")
        else:
            for i in range(x+1, y + 1, 2):
                print(i, end=" ")
    elif choice == 2:
        if x%2 == 0:
            for i in range(x+1,y+1,2):
                print(i,end = " ")
        else:
            for i in range(x, y + 1,2):
                print(i,end = " ")
    elif choice == 3:
        i = x
        while i <= y:
            square_root = i ** 0.5
            if  square_root%1 == 0:
                print(i,end = " ")
            i = i + 1
    elif choice != 4:
        print("Invalid Choice!")
    print()
