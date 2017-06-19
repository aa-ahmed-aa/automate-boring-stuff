#! python3
# pypdf2Test.py  - Open PDF and test PDF files 

#this example is reading regular pdf file
'''
import PyPDF2

objectfile = open('example.pdf','rb')
pdfreader = PyPDF2.PdfFileReader(objectfile)
print(pdfreader.numPages)

pageObj = pdfreader.getPage(0)
print(pageObj.extractText())
'''

#this example is reading encrypted pdf file
import PyPDF2

objectfile = open('example.pdf','rb')

pdfreader = PyPDF2.PdfFileReader(objectfile)

#for testing if this file is encrypted
#print(pdfreader.isEncrypted)

#check if the file is encrypted and decrypt it else show it 3ady
if pdfreader.isEncrypted==True:
	pdfreader.getPage(0).decrypt('rosebud') #algorith that will perfrom decryption
else:
	print(pdfreader.getPage(0).extractText())



