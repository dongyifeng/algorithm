#coding:utf-8

def swap(data,i,j):
	tmp = data[i]
	data[i] = data[j]
	data[j] = tmp

def isOddNumber(d):
	return d % 2 != 0
# 组数数组奇数位迁移，偶数位后移
def run(data):
	n = len(data) - 1
	i = 1
	if not isOddNumber(len(data)):
		j = n-1
	else:
		j = n
	while i < j:
		swap(data,i,j)
		i += 2
		j -= 2

data = [1,2,3,4,5,6]
run(data)
print data

data = [1,2,3,4,5,6,7]
run(data)
print data

def run(data):
	i = 0
	j = len(data) -	1
	while i < j:
		if isOddNumber(data[i]):
			i +=1
		elif not isOddNumber(data[j]):
			j -=1
		else:
			swap(data,i,j)

data = [2,1,7,3,6,5,4,9,6]
						
print run(data)
print data
