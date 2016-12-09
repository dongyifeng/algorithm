#coding:UTF-8
# 合并排序
import sys

def sort(data,start,end):
	if start >= end:return
	middle=(start+end)/2
	sort(data,start,middle)	
	sort(data,middle+1,end)
	merge(data,start,middle,end)	

def merge(data,start,middle,end):
	if start>middle or middle>end :return
	before=data[start:middle+1]
	after=data[middle+1:end+1]
	before.append(sys.maxsize)
	after.append(sys.maxsize)
	ai=bi=0
	for i in range(start,end+1):
		if before[bi]<after[ai]:
			data[i]=before[bi]
			bi+=1
		else:
			data[i]=after[ai]
			ai+=1

data=[2,8,7,1,3,5,6,4]
print data
sort(data,0,len(data)-1)
print data
