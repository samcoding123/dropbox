import os
import shutil
path = input("enter the name of the directry to be storted")
#list of files in the directory

list_of_files = os.listdir(path)
for file in list_of_files: 
    name,ext = os.path.splittext(file)
    ext = ext[1:]

    if ext == '':
        continue
    if os.path.exists(path+'/'+ext)
        shutil.move(path+'/'+file,path+'/'+ext+'/'+file)
    else:
        os.mkdirs(path+'/'+ext)
        shutil.move(path+'/'+file,path+'/'+ext+'/'+file)