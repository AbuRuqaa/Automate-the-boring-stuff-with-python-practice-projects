#!Python3
'''Write a program that walks through a folder tree and searches for exceptionally large files or folders—say, ones that have a file size of more than 100MB. 
(Remember that to get a file’s size, you can use os.path.getsize() from the os module.) Print these files with their absolute path to the screen.'''

import os
from send2trash import send2trash
from pathlib import Path as path


def spamFiles(folder):
    
    for foldersname,subfolders,filenames in os.walk(folder):
        for file in filenames:
            file=folder/file
            if not os.path.exists(file):
                continue
            elif os.path.getsize(file)>100000000:  
                print('Deleting: ',os.path.abspath(file),'...')
                #send2trash(file)#uncomment it after testing
                
                
spamFiles(path(r'C:\Users\Administrator\Downloads'))
                
    
    
    