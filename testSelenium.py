#! python3
# testSelenium.py - Open FireFxwebdriver for testing selenium
from selenium import webdriver
browser = webdriver.Firefox()
browser.get('http://inventwithpython.com')

try:
	elem = browser.find_element_by_class_name('bookcover')
	print('Found <%s> element with class name !' % elem.tag_name)
except:
	print("can't find elements ")