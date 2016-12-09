#coding:utf-8

# 元素最大间距。时间O(3*n),空间O(2*n)
# 最原始的思路：将数组排序，然后求元素之间最大查：排序O(nlogn)

import sys


def sortedRun(data):
	sorted(data)
	subject = - sys.maxsize
	for i in range(1,len(data)):
		if subject < data[i] -data[i-1]:
			subject = data[i] -data[i-1]
	return subject 

def run(data):
	# 求极值，为分桶做准备
	minValue =  sys.maxsize
	maxValue = - sys.maxsize
	for item in data:
		if item > maxValue:
			maxValue = item
		if item < minValue:
			minValue = item
	if maxValue == minValue:return 0

	# 确定桶的宽度
	n = len(data)
	d = (maxValue  - minValue)/(n + 1)
	bucket = [[] for i in range(n+1)]
	bucketExtreme = [[] for i in range(n+1)]
	bucket[0].append(minValue)
	bucket[n].append(maxValue)

	bucketExtreme[0] = [minValue,minValue]
	bucketExtreme[n] = [maxValue,maxValue]
	
	# 分桶，并且记录每个桶中最大值和最小值
	for item in data:
		if item == minValue or item == maxValue:continue
		b = int(item / d)
		bucket[b].append(item)
		if len(bucket[b]) == 1:
			bucketExtreme[b] = [item,item]
		else:
			if bucketExtreme[b][0] > item:			
				bucketExtreme[b][0] = item
			if bucketExtreme[b][1] < item:
				bucketExtreme[b][1] = item
	
	# 找最大的连续空桶的数
	tmpStartIndex = 0
	tmpEndIndex = 0
	marginNum = 0
	for i in range(len(bucket)):
		if len(bucket[i])>0:
			if tmpEndIndex - tmpStartIndex > marginNum:
				marginNum = tmpEndIndex - tmpStartIndex
				startIndex = tmpStartIndex
				endIndex = tmpEndIndex
			else:
				tmpStartIndex = tmpEndIndex = i	
			continue
		tmpEndIndex += 1
	return bucketExtreme[endIndex][0] - bucketExtreme[startIndex][1]

data = [0,2,4,100,150,200]
print run(data)
data = [0,2,4,100,150,200]
print sortedRun(data)

			
