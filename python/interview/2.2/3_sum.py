#coding:utf-8

#3-sum问题
#给定一个整数数组，判断能否从中找出3个数a、b、c，使得他们的和为0，如果能，请找出所有满足和为0个3个数对

import baseline


def swap(data,i,j):
	tmp = data[i]
	data[i] = data[j]
	data[j] = tmp

def handle(data):
	n = len(data)
	for i in range(n):
		swap(data,0,i)
		print '2_sum',data[0],baseline.run(data,-data[0],1,n-1)
		swap(data,0,i)
	
data = [1,2,4,7,-3,15,14,-6]
handle(data)
