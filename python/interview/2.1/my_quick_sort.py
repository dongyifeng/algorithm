#coding:utf-8

def swap(data,i,j):
	tmp = data[i]
	data[i] = data[j]
	data[j] = tmp

def run(data,s,e,k):
	if s >= e:return
	last = data[e]
	j = s

	for i in range(s,e):
		if data[i] <= last:
			swap(data,i,j)
			j += 1
	swap(data,j,e)
	if j == k:return data[j]
	if j > k:return run(data,s,j-1,k)
	if j < k:return run(data,j+1,e,k)

data = [4,2,8,1,3,1,6]
print data
# 显示
print 'result:',run(data,0,len(data)-1,2)
print 'result:',run(data,0,len(data)-1,5)
print data

