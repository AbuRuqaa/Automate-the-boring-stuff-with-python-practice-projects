#python3
'''Write a program that opens all .txt files in a folder and searches for any line that matches a user-supplied regular expression. The results should be printed to the screen.'''
from pathlib import Path as path
import time,re

while True:#Ask the user what kind of stuff he want to search for
    user=input('''Hello if you want to search for an email pls enter "email".\n\nif you want to search for a phone number pls enter"phone".\n\nor if you want something specfic pls type it:\n''')
    if user.lower()=='email':
        newRegex=re.compile(r'[a-zA-Z0-9]+@[a-z0-9]+\.[a-z]+')
        userSaid='email'
        break
    if user.lower()=='phone':
        newRegex=re.compile(r'\d{3}-\d{3}-\d{4}|\d{10}')
        userSaid='phone'
        break
    if not user:
        print('Please enter something')
        continue
    if user:
        newRegex=user
        userSaid='another'
        break
    
print('\n\nSearching...')
time.sleep(3)

folderPath=path(r'C:\Users\Administrator\Desktop\The long journey of programing\quizes\Mainexam')#The path for your folder where the files are

FileRegex=re.compile(newRegex)#The thing that you want to search for

globFile=list(folderPath.glob('*.txt'))#This line ensures that the program will open only a .txt file
words=[]

#Create a loop the will loop over all files that ends with .txt and open them then if anything matches with the Regex it will add it to 'words'

for i,n in enumerate(globFile):
    openFile=open(folderPath/str(n))
    readFile=openFile.read()  
    if FileRegex.search(readFile):
        words+=list(['\nFile number: '+str(i+1)+': \n'])+FileRegex.findall(readFile)
        
print('\n'.join(words))
    
    
   
    
    


     