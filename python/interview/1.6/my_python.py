
def swap(data,i,j):
	tmp = data[i]
	data[i] = data[j]
	data[j] = tmp

def handle(data,s,e):
	print s,e
	if s >= e-1:
		print data[s]

	for i in range(s,e):
		swap(data,0,i)
		handle(data,s+1,e)	
		

data = ['A','B','C']
handle(data,0,len(data))	
