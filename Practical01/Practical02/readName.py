file_name = open("name.txt","r")
name = file_name.read().strip()
print("Your name is",name)
file_name.close()
