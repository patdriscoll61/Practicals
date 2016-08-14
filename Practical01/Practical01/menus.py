
name = input("Enter name: ")
choice = "H"

while choice == "H" or choice == "G":

    print("(H)ello")
    print("(G)oodbye")
    print("(Q)uit")

    choice = input()
    choice = choice.upper()

    if choice == "H":
        print("Hello",name)
    elif choice == "G":
        print("Goodbye",name)
    elif choice != "Q":
        print("Invalid choice")
        choice = "H"
    else:
        print("")

