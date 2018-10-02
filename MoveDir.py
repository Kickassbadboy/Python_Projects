# Create a search within directory with Parameter(Screen Shot, .png).
#Author Yash Talegaonkar
# The Working The directory will first search the name screen shot and then if it passes then it will
# Pass to .png format regex . Then it will select the files and the move it within another directory

import os
import shutil
path=raw_input("Enter the path you want to copy file from: ")
new_path = raw_input("Enter the destination path: ")
files_in_path = os.listdir(path) # stores the name of all files inside path in a list
print(files_in_path)
#shutil.copytree(path,new_path) # Recursively copy an entire directory tree rooted at "path". The destination directory, named by "new_path", MUST NOT already exist

for file_name in files_in_path:
    file_path = os.path.join(path, file_name)
    print(file_path)
    if os.path.isfile(file_path):
        print(os.path.isfile(file_path))
        shutil.copy2(file_path, new_path) # destination directory MUST already exist