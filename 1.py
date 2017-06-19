import random     #to access random numbers
import sys        #to access sys functinos 
import pprint     #for better representation of the list and dictionary
import re         #for the regular expression functions
import shelve     #better dealling with files like database
import pyperclip  #to work with e clipboard stuff
import shutil     #to copy ,move files or folders
import send2trash # to save deleting files by sending to the trash
import zipfile    # to work with zipfiles extracting and compressing
import logging    # this library is used for logging to the console
import webbrowser # to open webbrowser and make stuff


def printBox(symbole, width, height):
	if len(symbole) > 1:
		raise Exception('the symbole must be only one character')
	if width <= 2:
		raise Exception('the width should be greater than 2')
	if  height <= 2:
		raise Exception('the height should be greater than 2')

	print (symbole * width)
	for i in range(height-2):
		print(symbole + ( ' '*(width-2) ) + symbole)
	print (symbole* width)

for s, w, h in (('*', 8, 8),('@',5 ,5),('87',1 ,1),('-',2 , 6)):
	try:
		printBox(s, w, h)
	except Exception as err:
		print('An error occured : '+ str(err))  
