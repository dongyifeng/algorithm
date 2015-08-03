#coding:UTF-8
# 桶排序
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
	

def exchange(data,i,j):
	tmp=data[i]
	data[i]=data[j]
	data[j]=tmp

data=[6,5,7,25,22,21,28]
print data
sort(data)
print data
