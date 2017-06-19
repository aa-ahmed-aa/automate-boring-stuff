#! python3
# maplty.py - launshed a map in the brwoser using an addess from 
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
 
if len(sys.argv) > 1:
	# get the address from the command
	address = ' '.join(sys.argv[1:])
else:
	#get the address from the clipboard
	address = pyperclip.paste()

webbrowser.open('http://google.com/maps/place/'+ address)