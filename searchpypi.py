#! python3
# searchpypi.py  - Opens several search results.
import requests, sys, webbrowser
sys.path.append(r"C:\Users\dell\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\site-packages")
from bs4 import BeautifulSoup

print('Searching...')    # display text while downloading the search result page
res = requests.get('https://pypi.org/search/?q='
+ ' '.join(sys.argv[1:]))
res.raise_for_status()
# TODO: Retrieve top search result links.
soup = BeautifulSoup(res.text,'html.parser')
print(soup.text)
# TODO: Open a browser tab for each result.
linkElems = soup.select('.package-snippet')
print(linkElems)
numOpen = min(5,len(linkElems))

for i in range(numOpen):
    urlToOpen = 'https://pypi.org' + linkElems[i].get('href')
    print('Opening', urlToOpen)
    webbrowser.open(urlToOpen)
    
