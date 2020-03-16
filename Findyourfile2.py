#This project find any png file and put it in a specific folders

import os, shutil, re
from pathlib import Path as path

## TODO:
#Make a for loop which will walk over all files on a specific folder then get it then rename it
#Make a regex which will find the png extension

def move(folder):
    folder=os.path.abspath(folder)
    fileRegex=re.compile(r'.*.png|jpg')#Regex which will get the file extension that you want
    destinsion1=path(r'Where you want to put your files')
    folWalk=os.listdir(path(r'the folder that contain the files you want to rename(same as destinsion1)'))#Get all the files path's (used to rename files)
    for folders,subfolders,files in os.walk(folder):#walk through all folder,subfolders,files in the given dir
        for file in files:#Walk through every file in files list
            file=folders+'\\'+file#Get the full path for the file
            fileBaseName=os.path.basename(file)
            des=destinsion1/fileBaseName
            mo=fileRegex.search(file)

            if not os.path.exists(file):
                continue
            if not mo:
                continue
            if mo:#Copying files
                print(f"Moving {fileBaseName} to {des}\n\n")
                #shutil.copy(file,f"{destinsion1}")uncomment this after check



    if mo:
        x=1
        for i in folWalk:#Renameing files
            print(folWalk)
            fullPath=destinsion1/i
            fileType=fullPath.suffix#get the file extension
            fileNewname=destinsion1/f'Picture({x}){fileType}'
            x+=1
            print(f'Renameing  {i} to Picture{x}\n\n')
            #os.rename(destinsion1/i,fileNewname)uncomment this after check








move(path(r'Your folder that the file you want to search for here(Put the path)'))
