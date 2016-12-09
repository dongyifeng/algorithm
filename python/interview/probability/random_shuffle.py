#coding:utf-8

# 随机排列产生
import random
a = [1,2,3,4,5,6,7]
random.shuffle(a)
print a

# 方法一：产生一个[1,n!]的随机数，然后求出一个排列
# 方法二：
#	初始值
#	a[i] 和a[i..n-1] 交换

def swap(data,i,j):
	tmp = data[i]
	data[i] = data[j]
	data[j] = tmp

def shuffle(array):
	n = len(array) - 1
	for i in range(n):
		swap(array,i,random.randint(i,n))

a = [1,2,3,4,5,6,7]
shuffle(a)
print a
