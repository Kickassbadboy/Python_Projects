import os
files=os.listdir('./')
for n in files:
    os.rename(n,n.replace(' ','_'))

