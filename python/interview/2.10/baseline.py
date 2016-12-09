#coding:utf-8
		

# 查找局部极小值
# 理解二分查找
# 已知数组a不重复。
# 利用结论：如果子数组a[x..y]，若a[x] < a[x-1] and a[y] < a[y+1]，则a 中有极小值

import sys

def getMin(a,s,e):
	if s>=e:return a[e]
	mid = (s+e)/2
	if a[mid] < a[mid+1]:
		return getMin(a,s,mid)
	else:
		return getMin(a,mid+1,e)
	
a = [sys.maxsize,1,2,3,4,5,0.1,2,5,sys.maxsize]
print getMin(a,0,len(a)-1)
