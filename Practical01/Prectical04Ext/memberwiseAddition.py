
def main():
    list1 = [1,2,3]
    list2 = [1,2,3,4]
    print(memberwiseAddition(list1,list2))

def memberwiseAddition(list1, list2):
    new_list = []
    list_length = len(list1)
    if len(list2) > list_length:
        list_length = len(list2)
    for i in range(list_length):
        number1 = 0
        number2 = 0
        if i <= len(list1)-1:
            number1 = list1[i]
        if i <= len(list2)-1:
            number2 = list2[i]
        sum = number1 + number2
        new_list.append(sum)
    return new_list

main()