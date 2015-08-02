
def sort(data):
	for i in range(1,len(data)):
		k=i
		current=data[i]
		while k>0 and current<data[k-1]:
			data[k]=data[k-1]
			k-=1
		data[k]=current

def exchange(data,i,j):
	tmp=data[i]
	data[i]=data[j]
	data[j]=tmp

data=[1,7,3,6,4,5]
print data
sort(data)
print data
