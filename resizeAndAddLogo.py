#!  python3
#resizeAndAddLogo.py - open and resize all odf the images in the folder and paste logo
import os
from PIL import Image

SQUARE_FIT_SIZE = 300
LOGO_FILENAME = 'logo.png'

logoIm = Image.open(LOGO_FILENAME)
logoWidth, logoHeight = logoIm.size

#loop over all the files 
for filename in os.listdir('.'):
	if not (filename.endswith('.png') or filename.endswith('.jpg')) or filename==LOGO_FILENAME:
		continue  #skip non image files 
	im = Image.open(filename)
	width, height = im.size

	#check if the image needs to be resized
	if width > SQUARE_FIT_SIZE and height > SQUARE_FIT_SIZE:
		#Calculate the new width and height to resize to.
		if width > height:
			height = int((SQUARE_FIT_SIZE / width)*height)
			width = SQUARE_FIT_SIZE
		else:
			width = int((SQUARE_FIT_SIZE / width)*height)
			height = SQUARE_FIT_SIZE

		#resze the image
		print("Resizing %s..." % (filename))
		im = im.resize((width,height))

	#add the logo
	print('Adding Logo to %s ..'%filename)
	im.paste(logoIm, (width - logoWidth , height - logoHeight), logoIm)

	#save changes
	im.save(os.path.join('withlogo', filename)) 