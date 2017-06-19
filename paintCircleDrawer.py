#! python3
#paintCircleDrawer.py - Draw circle in paint
#! python
# paintDrawer.py to test drawing in paint
import pyautogui,time
import math, sys

time.sleep(5)

pyautogui.click()	#click to put paint in focus
x, y = pyautogui.position()
radius = 11
PI = 3.14
angle = 0.0

for i in range(40):
	for t in range(0,70):
		#pyautogui.dragRel(x, y, duration=0.2) #move
		x = ( x + math.sin(angle) * radius)
		y = ( y + math.cos(angle) * radius)
		angle+=0.09
		pyautogui.dragTo(x, y, duration=0.0)
		print('X : %s , Y : %s' % (x,y))
	radius = radius - 1
	angle = 0.0
	x = x + 10
	pyautogui.moveTo(x, y, duration=0.0)
