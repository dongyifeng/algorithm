#coding:UTF-8
# 桶排序
import sys
def sort(data):
	bucket=[[]for i in range(10)]
	for i in range(len(data)):
		index=data[i]%10
		bucket[index].append(data[i])
		j=len(bucket[index])-1
		while bucket[index][j]<bucket[index][j-1] and j>0:
			bucket[index][j]=bucket[index][j-1]
			j-=1
		bucket[index][j]=data[i]
	k=0
	data=[0 for i in range(len(data))]
	data[0]=-sys.maxsize
	for i in range(10):
		if len(bucket[i])==0:continue
		print 'bucket:',bucket[i]
		for j in range(len(bucket[i])):
			#if bucket[i][j]>=data[k]:
			#	data[k]=bucket[i][j]
			#	k+=1
			#	continue
			h=k
			current=bucket[i][j]
			while h>0 and data[h]>current:
				data[h+1]=data[h]
				if h>0:h-=1
			print 'h',h
			data[h]=current
			k+=1
			print data
				

def exchange(data,i,j):
	tmp=data[i]
	data[i]=data[j]
	data[j]=tmp

data=[6,5,7,25,22,21,28]
print data
sort(data)
print data
