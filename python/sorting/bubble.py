# coding:UTF-8
# 冒泡排序
def sort(data):
	for i in range(len(data)):
		for j in range(i+1,len(data)):
			if data[i]>data[j]:
				exchange(data,j,i)

def exchange(data,i,j):
	tmp=data[i]
	data[i]=data[j]
	data[j]=tmp

data=[1,7,3,6,4,5]
print data
sort(data)
print data
