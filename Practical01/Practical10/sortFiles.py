"""
CP1404/CP5632 Practical
Sort files by extension - move to folder matching their extensions
"""
import os, shutil

__author__ = 'Patrick Driscoll'

def main():

    os.chdir('FilesToSort')
    file_extensions = []
    for filename in os.listdir('.'):
        # ignore directories, just process files
        if not os.path.isdir(filename):
            split_file_name = filename.rsplit(".")
            file_extension = split_file_name[-1]
            #print(file_extension)
            if file_extension not in file_extensions:
                file_extensions.append(file_extension)
                os.mkdir(file_extension)
            shutil.move(filename,file_extension+"/"+filename)
    print(file_extensions)

main()
