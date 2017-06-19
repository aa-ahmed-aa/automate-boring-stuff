#! python3
import time
def calcprod():
	product = 1;
	for i in range(1,100000):
		product = product * i
	return product


starttime = time.time()
prod = calcprod()
endtime = time.time()

print("the olength of product is %s " % len(str(prod)))
print("the excecution takes %s seconds.."%str(endtime-starttime))