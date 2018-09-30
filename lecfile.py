import os
path = raw_input("enter dir")
osdir = os.listdir(path)
for file in osdir:
    if ' ' in file:
        tmp = file.replace(' ', '_')
        os.rename(file, tmp)
        os.system('ls')