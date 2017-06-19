#! python3
# countDOwnAlarm.py - Countdown and then opens an alarm
import time, subprocess

timeleft = 60
while timeleft> 0 :
	print(timeleft, end=' ')
	time.sleep(1)
	timeleft = timeleft - 1

#At the end of the countdown, play a sound file
subprocess.Popen(['start','alarm.mp3'], shell=True)