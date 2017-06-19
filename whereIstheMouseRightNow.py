#! python
# whereIstheMouseRightNow.py - to return the mouse position now
import pyautogui

print('Press Ctrl-C to quit')
#Get and print the mouse coordinates
try:
	while True:
		x, y = pyautogui.position()
		positionStr = 'X: '+str(x).rjust(4)+'   Y: '+str(y).rjust(4)
		print(positionStr, end='')
		print('\b'*len(positionStr), end='', flush=True)  
except KeyboardInterrupt:
	print('\nDone.')