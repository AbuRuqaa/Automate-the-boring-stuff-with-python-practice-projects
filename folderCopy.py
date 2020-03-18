#python 3
'''Write a program that walks through a folder tree and searches for files with a certain file extension (such as .pdf or .jpg). Copy these files from whatever location they are in to a new folder.'''
import re,os,shutil
from pathlib import Path as path


def search(folder):
   extensionPattern=re.compile('(.*?).(pdf)?(jpg)?')#createing the regex
    
    for foldernames,subfolders,filenames in os.walk(folder):#Create a walking directory that will go through every folder and file in the give "folder"
        for file in filenames:
            file=folder+'/'+file #Create the file path if not the file will be just the basename
            mo=extensionPattern.search(file)#Search for a file that's that same as the regex
            if mo==None:#If file is not like the regex then skip it and move to the next one
                continue
            if mo:
                print(f'Copying {file} to C:\\Users\Administrator\\Desktop\\The long journey of programing\\hi...')
                shutil.copy(file,r'C:\Users\Administrator\Desktop\The long journey of programing\hi')
            
            
search(r'C:\Users\Administrator\Desktop\picture')
    
    
        