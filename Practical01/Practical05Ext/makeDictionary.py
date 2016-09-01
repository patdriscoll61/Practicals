def main():
    names = ["Jack", "Jill", "Harry"]
    dobs = [(12, 4, 1999), (1, 1, 2000), (27, 3, 1982)]

    dob_dict = make_list(names, dobs)
    print(dob_dict)


def make_list(keys, values):
    my_dict = dict(zip(keys, values))
    return my_dict


main()
