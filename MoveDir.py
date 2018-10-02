# Create a search within directory with Parameter(Screen Shot, .png).

# The Working The directory will first search the name screen shot and then if it passes then it will
# Pass to .png format regex . Then it will select the files and the move it within another directory

import os
import shutil
path=raw_input("Enter the path you want to copy file from")
new_path = raw_input("Enter the destination path")
current_path = os.listdir(path) # it creates variable to store the current path
for files in current_path:
    all_files = os.path.join(current_path,path)
    if os.path.isfile(all_files):
        shutil.copy(all_files,new_path)