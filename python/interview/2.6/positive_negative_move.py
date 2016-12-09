#coding:utf-8

#一个未排序整数数组，有正负数，重新排列使负数排在正数前面，并且要求不改变原来的正负数之间相对顺序，比如： input: 1,7,-5,9,-12,15 ans: -5,-12,1,7,9,15 要求时间复杂度O(n),空间O(1)。 

# 这个算法并没有满足O(n)
def run(data):
	if data is None or len(data) == 0:return
	for i in range(len(data)):
		if data[i] >= 0:continue
		j = i
		current = data[i]
		while j > 0 and data[j-1]>0:
			data[j] = data[j-1]
			j -= 1
		data[j] = current

data = [1,7,-5,9,-12,15]
print data
run(data)
print data

