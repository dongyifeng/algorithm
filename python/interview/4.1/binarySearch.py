#coding:utf-8

def binarySearch(data,s,e,v):
	if data is None or s > e:
		return -1
	m = (s + e) / 2
	if data[m] == v:
		return m
	if data[m] < v:
		return binarySearch(data,m+1,e,v)
	return binarySearch(data,s,m-1,v)

data = [1,2,3,4,5,6]
print binarySearch(data,0,len(data)-1,5)
print binarySearch(data,0,len(data)-1,5.1)
