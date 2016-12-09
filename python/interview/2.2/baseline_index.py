#coding:utf-8
# 返回所有满足的下标

def run(data,k,s,e):
	h = {}
	i = s
	j = e
	while i < j:
		h[k-data[i]] = i
		h[k-data[j]] = j
		i += 1
		j -= 1
	i = 0
	j = len(data) - 1
	print h
	result = set() ;
	while i < j:
		if data[i] in h and i != h[data[i]]:
			result.add((i,h[data[i]]))
			break
		if data[j] in h and j !=h[data[j]]:
			result.add((j,h[data[j]]))
			break
		i += 1
		j -= 1

	return result
data = [3,2,4]
print data
print run(data,6,0,len(data)-1)
	
