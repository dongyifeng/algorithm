#coding:utf-8

# 类似快排的做法，两个指针:i,j 同时从左向右


def swap(data,i,j):
	tmp = data[i]
	data[i] = data[j]
	data[j] = tmp

def isOddNumber(d):
	return d % 2 != 0

def run(data):
	j = 0
	for i in range(0,len(data)):
		if isOddNumber(data[i]):
			swap(data,i,j)
			j += 1


data = [2,1,7,3,6,5,4,9,6]
print 'raw',data
print run(data)
print data
