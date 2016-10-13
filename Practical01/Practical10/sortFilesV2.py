"""
CP1404/CP5632 Practical
Sort files by extension - move to folder matching their extensions
"""
import os, shutil

__author__ = 'Patrick Driscoll'

def main():

    # Get a dictionary of extensions and folder names and make folders
    os.chdir('FilesToSort2')
    file_extensions = {}
    folders = []
    for filename in os.listdir('.'):
        # ignore directories, just process files
        if not os.path.isdir(filename):
            split_file_name = filename.rsplit(".")
            file_extension = split_file_name[-1]
            if file_extension not in file_extensions:
                folder = input("What category would you like to sort {} files into? ".format(file_extension))
                file_extensions[file_extension] = folder
                if folder not in folders:
                    folders.append(folder)
                    os.mkdir(folder)

    #print(file_extensions)
    #print(folders)

    # move files
    for filename in os.listdir('.'):
        # ignore directories, just process files
        if not os.path.isdir(filename):
            split_file_name = filename.rsplit(".")
            file_extension = split_file_name[-1]
            folder = file_extensions[file_extension]
            shutil.move(filename,folder+"/"+filename)


main()
