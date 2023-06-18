#!/usr/bin/env python

import argparse
import os

parser = argparse.ArgumentParser(description='gets the logs for the given file path')

parser.add_argument('path',
                    metavar='PATH',
                    type=str,
                    nargs="?",
                    help='Enter the path or file name whose log that you want to get')

args = parser.parse_args()

path = args.path 
print(path)

# checking if a path is a relative path or an absolute path

if path  == "current":
    path = os.getcwd()
    print(path)
    os.system(f'git log {path}')

else:
    print("Inside here")
    if os.path.isabs(path) == True:
        isExisting = os.path.exists(path)
        if isExisting:
            if os.path.isdir(path):
                os.chdir(path)
                os.system('git log')
            elif os.path.isfile(path):
                dir_name =  os.path.dirname(path)
                print(f"this is the dir name: {dir_name}")
                if dir_name != "":
                    os.chdir(dir_name)
                file_name = os.path.basename(path)
                os.system(f'git log {file_name}')
            else:
                print("Error in the tree structure")
        else:
            print("Path does not exist find the please give the correct path abs")


    elif os.path.isabs(path) == False:
        isExisting = os.path.exists(path)
        if isExisting:
            if os.path.isdir(path):
                os.chdir(path)
                os.system('git log')
            elif os.path.isfile(path):
                dir_name =  os.path.dirname(path)
                print(f"this is the dir name:{dir_name}")
                if dir_name != "":
                    os.chdir(dir_name)
                file_name = os.path.basename(path)
                os.system(f'git log {file_name}')
            else:
                print("Error in the tree structure")
        else:
            print("Path does not exist find the please give the correct path rel")
    else:
        print("folder or file inside the current working directory")


