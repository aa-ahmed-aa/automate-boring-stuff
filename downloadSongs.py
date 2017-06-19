#! python3
# downloadSongs - Download songs from freemusicarchive.com

import requests, bs4, os, pprint, re

os.makedirs('songs', exist_ok=True)

def downloadImage(link):
	file = open(os.path.join('songs', os.path.basename(link)+'.mp3' ) , 'wb')
	for chunk in requests.get(link).iter_content(100000):
		file.write(chunk)
	print ("file %s.mp3  saves.." % os.path.basename(link) )

def endOfThePage(soup):
	#this will determine if the end of the page was detected
	el = soup.select('.playlist')
	if not el:
		return False
	else:
		return True

link = 'http://freemusicarchive.org/genre/Soundtrack/'
soup = bs4.BeautifulSoup(requests.get(link).text,'html.parser')

while endOfThePage(soup):
	#Get the list of the current songs from the div 
	links = soup.select('.playicn .icn-arrow')
	ls = []
	for i in range(len(links)): 
		ls.append(links[i].get('href'))

	#Save the songs from the first page
	for i in range(len(ls)):
		downloadImage(ls[i])

	#find the next page
	next_page = soup.select('.pagination-full b a')
	next_page_link  = next_page[len(next_page)-1].get('href')
	print("iam now crawling page number %s " % re.search('page=([0-9]*)', os.path.basename(next_page_link), re.I|re.M).group(0) )

	#change the soup
	soup = bs4.BeautifulSoup(requests.get(next_page_link).text,'html.parser')