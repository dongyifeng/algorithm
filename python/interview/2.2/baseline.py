#coding:utf-8

def run(data,k,s,e):
	h = {}
	i = s
	j = e
	while i < j:
		h[k-data[i]] = data[i]
		h[k-data[j]] = data[j]
		i += 1
		j -= 1
	i = 0
	j = len(data) - 1
	while i < j:
		if data[i] in h:
			return (data[i],h[data[i]])
		if data[j] in h:
			return (data[j],h[data[j]])
		i += 1
		j -= 1

data = [1,2,4,7,11,15]
print run(data,15,0,len(data)-1)
	
