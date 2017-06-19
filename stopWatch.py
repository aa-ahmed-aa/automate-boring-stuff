#! python3
# stopWatch.py - stop watch using time library
import time 
import datetime

# Desplay the program's instructions 
print ('Press ENTER to begin ,Afterwards Press Enter to "click" the stop watch . Press Ctrl+C to quit')
input()
print('Started.')
startTime = time.time()
lastTime = startTime
lapNum = 1

#Start tracking the laptime
try:
	while True:
		input()
		lapTime = round(time.time() - lastTime, 2)
		totalTime = round(time.time() - startTime, 2)
		print('Lap #%s: %s (%s)' % (lapNum, totalTime, lapTime), end='')
		lapNum += 1
		lastTime = time.time() #reset the last lap time
except KeyboardInterrupt:
	#handle the Ctrl-C Exception and print Done 
	print('\nDone.')