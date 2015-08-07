# coding:UTF-8
# 插入排序
def sort(data):
	for i in range(1,len(data)):
		k=i
		current=data[i]
		while k>0 and current<data[k-1]:
			data[k]=data[k-1]
			k-=1
		data[k]=current

data=[1,7,3,6,4,5]
print data
sort(data)
print data
