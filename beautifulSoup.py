import bs4

file = open('index.html','r')
data = file.read()
element = bs4.BeautifulSoup(data, 'html.parser')

text = element.select('#link')

print(text[0].get('href'))
print(text[0].getText())