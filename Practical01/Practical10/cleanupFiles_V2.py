"""
CP1404/CP5632 Practical
File renaming and os examples
"""
import os, shutil

__author__ = 'Lindsay Ward'

def main():

    print("Current directory is", os.getcwd())

    # change to desired directory
    os.chdir('Lyrics')
    # print a list of all files (test)
    # print(os.listdir('.'))

    # make a new directory
    # os.mkdir('temp')

    #view_folders()

    # NOTE: os.walk() yields a 3-tuple (dirpath, dirnames, filenames)
    for dir_name, subdir_list, file_list in os.walk('.'):
        print("New Names Would Be For Folder ", dir_name)
        for filename in file_list:
            new_name = get_fixed_filename(filename)
            print(new_name)
            #os.rename(filename, new_name)
        print("****","\n")

def temp():
    # loop through each file in the (original) directory
    for filename in os.listdir('.'):
        # ignore directories, just process files
        if not os.path.isdir(filename):
            filename = get_fixed_filename(filename)
            print(filename)
            # Option 1: rename file to new name - in place
            # os.rename(filename, new_name)

            # Option 2: move file to new place, with new name
            # shutil.move(filename, 'temp/' + new_name)


def get_fixed_filename(filename):
    # Step 1 - Make extension lower case
    new_name = filename.replace(".TXT", ".txt")
    # Step 2 - Capitalise after a space
    temp_name = ""
    chars = {}
    for i,char in enumerate(new_name):
        chars[i] = char
        if i >= 1 and chars[i-1] == " ":
            temp_name += chars[i].upper()
        else:
            temp_name += chars[i]
    new_name = temp_name
    #print(chars)
    #return new_name
    # Step 3 - Add a Space before a cap if it s not there
    temp_name = ""
    chars = {}
    for i,char in enumerate(new_name):
        chars[i] = char
        if char.isupper():
            if i >= 1 and chars[i-1] != " " and chars[i-1] != "(":
                temp_name += " " + chars[i]
            else:
                temp_name += chars[i]
        else:
                temp_name += chars[i]
    new_name = temp_name
    # Step 4 - Replace space with underline character
    new_name = new_name.replace(" ", "_")
    return new_name


def view_folders():
    # Processing subdirectories using os.walk()
    #os.chdir('..')
    # NOTE: os.walk() yields a 3-tuple (dirpath, dirnames, filenames)
    for dir_name, subdir_list, file_list in os.walk('.'):
        print("In", dir_name)
        print("\tcontains subdirectories:", subdir_list)
        print("\tand files:", file_list)

main()