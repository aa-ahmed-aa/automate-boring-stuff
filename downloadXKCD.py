#! python3
# downloadXKCD - Downloads comics from xkcd.com

import bs4,requests, os

url = 'https://xkcd.com/'
os.makedirs('xkcd', exist_ok=True)

while not url.endswith('#'):
	#download the page
	page = requests.get(url)
	soup = bs4.BeautifulSoup(page.text, 'html.parser')

	#find the url of the comics
	comic_link = soup.select('#comic img')
	if comic_link == []:
		print('Couldn\'t find the image')
	else:
		comicUrl = comic_link[0].get('src')
		comic = 'http:' + comicUrl
		print('Downloading image %s ...' % comic)
		#downlaod the image
		res = requests.get(comic)

	#save the image to ./xkcd
	imagefile = open(os.path.join('xkcd',os.path.basename(comic)),'wb')
	for chunk in res.iter_content(100000):
		imagefile.write(chunk)
	imagefile.close()

	#get the previous button url
	prevLink = soup.select('a[rel="prev"]')[0]
	url = "https://xkcd.com" + prevLink.get('href')
	print (url)



print('--DONE--')