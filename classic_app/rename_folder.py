import os

for dir1 in os.listdir():
    dest =  ''.join(dir1.split(' ')) 
    os.rename(dir,dest)