#coding:UTF-8
# 快排
def sort(data,start,end):
	if start>=end:return
	i=start
	last=data[end]
	for k in range(start,end):
		if data[k]<=last:
			exchange(data,i,k)
			i+=1
	print data,start,end,i
	exchange(data,i,end)	
	sort(data,start,i-1)
	sort(data,i+1,end)
	

def exchange(data,i,j):
	tmp=data[i]
	data[i]=data[j]
	data[j]=tmp

data=[4, 2, 1, 3, 1]
print data
sort(data,0,len(data)-1)
print data
