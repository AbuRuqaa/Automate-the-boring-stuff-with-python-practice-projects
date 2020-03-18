#python 3
# searchpypi- Open serval search results

import requests,sys,os,bs4,webbrowser

print('Searching...')
res = requests.get('https://pypi.org/search/?q='+ ' '.join(sys.argv[1:]))
link='https://pypi.org/search/?q=requests'
res.raise_for_status()

#Retrieve top search result links.
soup=bs4.BeautifulSoup(res.text,'html.parser')

#Open a browser tap for each result.

linkElems = soup.select(".package-snippet")
numOpen=min(5, len(linkElems))
for i in range(len(linkElems[:30])):
    urlToOpen = 'https://pypi.org' + linkElems[i].get('href')
    print('Opening',urlToOpen)
    webbrowser.open(urlToOpen)
