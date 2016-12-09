#coding:utf-8

def run(data,k):
	if data is None or len(data) < 2:return
	i = 0
	j = len(data) - 1
	if data[j] + data[j-1] < k:return
	while i < j:
		if data[i] + data[j] > k:
			j -= 1
		if data[i] + data[j] < k:
			i += 1
		if data[i] + data[j] == k:
			return (data[i],data[j])

data = [1,2,4,7,11,15]
print run(data,26)
