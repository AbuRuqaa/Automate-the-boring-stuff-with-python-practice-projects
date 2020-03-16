#!python 3
#Images downloader

import os,requests
from bs4 import BeautifulSoup as bs
from pathlib import Path as path





def imgur():
    global imageName,fullLink

    url=f'https://imgur.com/search?q={user}'
    res=requests.get(url)#send requests
    res.raise_for_status()
    picSoup=bs(res.text,'html.parser')
    imgHtml=picSoup.select('img')#Want to download an img

    if imgNumber:
        for i in range(int(imgNumber)):
                photoLink=imgHtml[i].get('src')#Get the link
                fullLink=f'https:'+photoLink#Get the full link
                res=requests.get(fullLink)#Send request to the photo link

                print(f'\n\nDownloading {fullLink}')
                imageFile=open(os.path.join(r'C:\Users\Administrator\Desktop\pic_downloader\imgur',os.path.basename(fullLink)),'wb')
                imageName=os.path.join(r'C:\Users\Administrator\Desktop\pic_downloader\imgur',os.path.basename(fullLink))

                for chunk in res.iter_content(100000):
                        imageFile.write(chunk)
                imageFile.close()
                rename()
    if not imgNumber:
        for i in range(len(imgHtml)):
            photoLink=imgHtml[i].get('src')#Get the link
            fullLink=f'https:'+photoLink
            res=requests.get(fullLink)
            res.raise_for_status()
            print(f'\n\nDownloading {fullLink}')
            imageFile=open(os.path.join(r'C:\Users\Administrator\Desktop\pic_downloader\imgur',os.path.basename(fullLink)),'wb')
            imageName=os.path.join(r'C:\Users\Administrator\Desktop\pic_downloader\imgur',os.path.basename(fullLink))
            rename()
            for chunk in res.iter_content(100000):
                imageFile.write(chunk)
            imageFile.close()




def rename():
    renamePath=r'C:\Users\Administrator\Desktop\pic_downloader\imgur'
    global x


    fullPath=path(imageName)#get image full path
    fileType=fullPath.suffix#get the file extension
    fileNewname=path(r'C:\Users\Administrator\Desktop\pic_downloader\imgur')/f'{filesName}{x}{fileType}'

    while os.path.exists(fileNewname):#if file name already exsits (like if the user downloaded the pic before)
        x+=1#add 1 to x until it be bigger than the last file name
        try:
            fileNewname=path(r'C:\Users\Administrator\Desktop\pic_downloader\imgur')/f'{filesName}{x}{fileType}'#trying to create a new file name that is not used before by adding 1to x value


        except:
            pass
        if not os.path.exists(fileNewname):#if it found a new name then it will exit the loop
            break

    print(f'\n\nRenameing  C:\\Users\\Administrator\\Desktop\\pic_downloader\\imgur\\{os.path.basename(fullLink)} to {fileNewname}\n\n')
    os.rename(f'C:\\Users\\Administrator\\Desktop\\pic_downloader\\imgur\\{os.path.basename(fullLink)}',fileNewname)

    x+=1


def createFolder():
    try:#put try here just to make sure that the program won't crash if the folder is already exists
        os.makedirs(r'C:\Users\Administrator\Desktop\pic_downloader\imgur')#create a new folder on desktop

    except FileExistsError:
        pass
x=1
user=input("The name of the picture's that you want to download pls:\n")
imgNumber=input('How many images do you want to download?\n\n(if you want all dont type anything)\n')
filesName=input('Pls give us a name to rename the pictures:\n')

createFolder()
imgur()
