
def main():
    string = "dummy value"
    strings = []
    while string != "":
        string = input("Enter String: ")
        if string != "":
            strings.append(string)
    strings.sort()
    strings_repeated = []
    string = strings[0]
    #print("Length of strings {}".format(len(strings)))
    #print(strings)
    for i in range(2,len(strings)):
        string = strings[i]
        if string not in strings_repeated and i < len(strings)-1 and strings[i] == string:
            strings_repeated.append(string)
    if len(strings_repeated) > 0:
        print("Strings reapeated: ", end=" ")
        for i in range(len(strings_repeated)):
            print(strings_repeated[i], end=" ")
    else:
        print("No repeat strings were entered")


main()