#! python3
# multiThreading.py - is a multithreading test in python

'''
import threading, time

print("Start of the program")

def takeanap():
	time.sleep(5)
	print('Wake Up!')

threadObject = threading.Thread(target = takeanap)
threadObject.start()

print("End of the program")
'''

import threading,time

def countToTen():
	for i in range(10):
		print("counting %i :" % i)

threads=[]
for i in range(5):
	thread = threading.Thread(target=countToTen)
	thread.start()
	threads.append(thread)

for thread in threads:
	thread.join()

print("Done..")
