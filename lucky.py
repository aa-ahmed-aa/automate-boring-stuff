#! python3
# lucky.py - Opens several Google search results
import requests, sys, webbrowser, bs4

print('Googling....')
res = requests.get('http://google.com/search?q='+''.join(sys.argv[1:]))
res.raise_for_status()

#retrieve top search results
soup = bs4.BeautifulSoup(res.text, 'html.parser')

#open a browser tab for each result
linkElems = soup.select('.r a')
for i in range(5):
	webbrowser.open('http://google.com'+linkElems[i].get('href'))