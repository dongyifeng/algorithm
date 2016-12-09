#coding:utf-8

def swap(data,i,j):
	tmp = data[i]
	data[i] = data[j]
	data[j] = tmp

def run(data):
	n = len(data)
	k = i = 0
	j = n - 1
	while j > i and i >= k:
		if data[i] == 1:
			swap(data,i,k)	
			k += 1
		elif data[i] == 3:
			swap(data,i,j)
			print 'change 3',data,k,i,j
			j -= 1
		
		i += 1

data=[3,1,2,1,1,3,2,2,3]
run(data)
print data
