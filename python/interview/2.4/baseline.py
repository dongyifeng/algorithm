#coding:utf-8
import sys

def run(data):
	if data is None:return
	maxSum = - sys.maxsize
	n = len(data)
	for i in range(n):
		for j in range(i,n):
			currentSum = 0
			for k in range(i,j+1):
				currentSum += data[k]
			if currentSum >= maxSum:
				maxSum = currentSum		
	return maxSum

data = [1,-2,3,10,-4,7,2,-5]
print run(data)
