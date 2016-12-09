
def swap(data,i,j):
	tmp = data[i]
	data[i] = data[j]
	data[j] = tmp

def sort(data,s,e):
	if s >= e :return
	last = data[e]
	k = s 
	for i in range(s,e):
		if data[i] < last:
			swap(data,i,k)
			k+=1
		swap(data,s,k)
	sort(data,s,k-1)
	sort(data,k+1,e)

def containString(a,b):
	if len(a) < len(b):return False
	sort(a,0,len(a)-1)
	sort(b,0,len(b)-1)
	
	bi = 0
	for i in range(0,len(a)):
		if a[i] == b[bi]:
			bi+=1
	print bi
	return bi == len(b)

a=["A","B","C","E"]
b=["B","E"]
print containString(a,b)	
