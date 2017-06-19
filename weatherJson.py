#! python3
# weatherJson.py - to get the weather from openweathermap.org 
# for today and the next two days
import json, requests, sys, pprint

# compute location from the command line 
if len(sys.argv) < 2:
	print("Usage : weatherJson.py location")
	sys.exit()
location = ' '.join(sys.argv[1:])

#download th json data
url = 'http://api.openweathermap.org/data/2.5/forecast/daily?q=%s&cnt=3' % (location)
response = requests.get(url)

#load json into python variable
weatherData = json.loads(response.text)  
pprint.pprint(weatherData)