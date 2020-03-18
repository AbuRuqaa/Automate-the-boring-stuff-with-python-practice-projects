#!python 3
#Filling The Gaps
'''Write a program that finds all files with a given prefix, such as spam001.
txt, spam002.txt, and so on, in a single folder and locates any gaps in the numbering (such as if there is a spam001.txt and spam003.txt but no spam002.txt). 
Have the program rename all the later files to close this gap.
As an added challenge, write another program that can insert gaps into numbered files so that a new file can be added.'''
import re,os,shutil
from pathlib import Path as path

def prefix(folder):
    global newFilename
    numbersPattern=re.compile(r'(.*?)(\d{1,3})?(.txt)')
    os.chdir(folder)
    
    for file in os.listdir(folder):
        
        
        mo=numbersPattern.search(file)
        if mo==None:#If the file is not like the pattern then move to another file
            continue
        beforeGroup=mo.group(1)#Get the groups
        regexGroup=int(mo.group(2))
        afterGroup=mo.group(3)
    all_files = os.listdir(folder)
    all_files.sort()
    newDigit=1  
    for file in all_files:
        
        newFilename=folder+'/'+beforeGroup+str(newDigit)+'.txt'
        newDigit+=1
        dis=newFilename
        print(f'\n\n{newDigit}')
        source=os.path.join(folder,file)
        if newFilename in os.listdir(folder):
            print(f'Skipping {file}')
            continue
        else:
            print(f'\n\nRenaming: {source} to {dis}')
            shutil.move(file,f'{dis}')
        
prefix(r'C:\Users\Administrator\Desktop\The long journey of programing\quizes\answerforTheExam')
                
        
            
    
    
    
    