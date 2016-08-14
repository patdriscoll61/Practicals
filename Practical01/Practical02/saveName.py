name = input("What is your name? ")
file_name = open("name.txt","w")
print(name,file=file_name)
file_name.close()
