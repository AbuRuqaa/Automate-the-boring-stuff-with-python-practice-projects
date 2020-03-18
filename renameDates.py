#!python3
#renameDates.py Renames filename with American  MM-DD-YYYY date format
#to Eyropean DD-MM-YYYY.

# TODO: Loop over the files in the working directory.

# TODO: Skip files without a date.

# TODO: Get the different parts of the filename.

# TODO: Form the European-style filename.

# TODO: Get the full, absolute file paths.

# TODO: Rename the files.
from pathlib import Path as path
import os,shutil,re


p=path(r'C:\Users\Administrator\Desktop\The long journey of programing\testForRenameDates_projects')

#Create a regex that contains an American data format

datePattren=re.compile("""^(.*?)# all text before the date #group 1
                       ((0|1)?/d)- #one or two digits for the month 
                       ((0|1|2|3)?\d)- #one or two digits for the day
                       ((19|20)\d\d) #four digits for the year
                       (.*?)$ # all text after the daye
                       """,re.VERBOSE)



for amerFilename in os.listdir(p):
    mo=dataPattern.search(amerFilename)
    
    #Skip files with out name
    if mo==None:
        continue
    
    #Get the different parts of file name
    beforePart=mo.group(1)
    monthPart=mo.group(2)
    dayPart=mo.group(4)
    yearPart=mo.group(6)
    afterPart=mo.group(8)
    
    #Form the European-style filename.
    euroFilename=beforePart+dayPart+'-'+monthPart+'-'+yearPart+afterPart
    
    
    
    #Get the full,absolute file paths.
    absWorkingDir=os.path.abspath('.')
    amerFilename=os.path.join(absWorkingDir)
    euroFilename=os.path.join(absWorkingDir,euroFilename)
    
    #Rename the files.
    
    print(f'Renaming"{amerFilename}"to"{euroFilename}""...')
    #shutil.move(amerFilename,euroFilename)#Uncomment after testing
    
    
    