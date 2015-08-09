#coding:UTF-8
# 桶排序
import sys
def sort(data):
	bucket=[[]for i in range(10)]
	# 将数据放入桶中
	for i in range(len(data)):
		index=data[i]%10
		bucket[index].append(data[i])
		j=len(bucket[index])-1
		while bucket[index][j]<bucket[index][j-1] and j>0:
			bucket[index][j]=bucket[index][j-1]
			j-=1
		bucket[index][j]=data[i]
	# 将桶中数据放回数组
	k=0
	for i in range(10):
		if len(bucket[i])==0:continue
		for j in range(len(bucket[i])):
			data[k]=bucket[i][j]
			h=k-1
			while h>=0 and bucket[i][j]<data[h]:
				exchange(data,h,h+1)
				h-=1
			k+=1

def exchange(data,i,j):
	tmp=data[i]
	data[i]=data[j]
	data[j]=tmp

data=[6,5,7,25,22,21,28]
print data
sort(data)
print data
