#!python3

#downloadXkcd- Downloads every single XKCD comic

import requests,os,bs4
from pathlib import Path as path
url='https://xkcd.com'

os.makedirs(path.home()/'Desktop'/'xkcd',exist_ok=True)

while not url.endswith('#'):
    #Downloading the page.
    print(f'Downloding page {url}')
    res=requests.get(url)
    res.raise_for_status()

    soup=bs4.BeautifulSoup(res.text,'html.parser')

    #Find the url of the comic image.
    comicElem=soup.select('#comic img')
    if comicElem==[]:
        print('Could not find comic image')
    else:
        comicUrl='https:'+comicElem[0].get('src')
        #downloading the image.
        print(f'Downloading image {comicUrl}')
        res=requests.get(comicUrl)
        res.raise_for_status()

        imageFile=open(os.path.join(r"C:\Users\Administrator\Desktop\xkcd" ,os.path.basename(comicUrl)),'wb')
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()

        #Get the prev button's url.
        prevLink=soup.select('a[rel="prev"]')[0]
        url='https://xkcd.com'+prevLink.get('href')

print('Done')
