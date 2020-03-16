#This project find any png file and copy it in a specific folders
#after that it rename the files

import os, shutil, re
from pathlib import Path as path

## TODO:
#Make a for loop which will walk over all files on a specific folder then get it then rename it
#Make a regex which will find the png extension

def move(folder):
    folder=os.path.abspath(folder)

    fileRegex=re.compile(r'.*.png|jpg')#Regex which will get the file extension that you want

    destinsion1=path(r'C:\Users\Administrator\Desktop\pic1')#Where you want to put your files



    for folders,subfolders,files in os.walk(folder):#walk through all folder,subfolders,files in the given dir
        for file in files:#Walk through every file in files list
            file=folders+'\\'+file#Get the full path for the file
            fileBaseName=os.path.basename(file)
            des=destinsion1/fileBaseName
            mo=fileRegex.search(file)
            print(file)
            if not os.path.exists(file):
                continue
            if not mo:
                continue
            if mo:#Copying files
                #print(f"Moving {fileBaseName} to {des}\n\n")
                #shutil.copy(file,f"{destinsion1}")#uncomment this after check
                pass



def rename():
    folWalk=os.listdir(path(r'C:\Users\Administrator\Desktop\pic1'))#the folder that contain the files you want to rename(same as destinsion1)
    filePath=path(r'C:\Users\Administrator\Desktop\pic1')
    x=1
    for i in folWalk:#Renameing files
        fullPath=filePath/i
        fileType=fullPath.suffix#get the file extension
        fileNewname=filePath/f'Picture({x}){fileType}'
        x+=1
        print(f'Renameing  {i} to Picture ({x})\n\n')
        os.rename(filePath/i,fileNewname)#uncomment this after check








move(path(r'C:\Users\Administrator\Pictures'))#'Your folder that the file you want to search for here(Put the path)
#rename()
