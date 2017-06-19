#! python3
# downloadStuff.py - to download stuff from the web 
# the command line 
import random     #to access random numbers
import sys        #to access sys functinos 
import pprint     #for better representation of the list and dictionary
import re         #for the regular expression functions
import shelve     #better dealling with files like database
import pyperclip  #to work with e clipboard stuff
import shutil     #to copy ,move files or folders
import send2trash #to save deleting files by sending to the trash
import zipfile    #to work with zipfiles extracting and compressing
import logging    #this library is used for logging to the console
import webbrowser #to open webbrowser and make stuff
import requests   #the web requests package for 
 
res = requests.get('https://www.gutenberg.org/cache/epub/1112/pg1112.txt')

try:
	res.raise_for_status()
	playfile = open('a1.txt','w')
	for chunk in res.iter_content(1000):
		playfile.write(str(chunk))
	playfile.close()
except Exception as exc:
	print('There was a problem : %s' % (exc))