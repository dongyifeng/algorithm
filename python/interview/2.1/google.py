#coding:utf-8
#谷歌面试题：输入是两个整数数组，他们任意两个数的和又可以组成一个数组，求这个和中前k个数怎么做？ 

#“假设两个整数数组为A和B，各有N个元素，任意两个数的和组成的数组C有N^2个元素。
#   那么可以把这些和看成N个有序数列：
#          A[1]+B[1] <= A[1]+B[2] <= A[1]+B[3] <=…
#          A[2]+B[1] <= A[2]+B[2] <= A[2]+B[3] <=…
#          …
#         A[N]+B[1] <= A[N]+B[2] <= A[N]+B[3] <=…
#    问题转变成，在这N^2个有序数列里，找到前k小的元素”

import my_quick_sort

def generateSum(data1,data2):
	result = []
	for i in data1:
		for j in data2:
			result.append(i+j)
	return result



data1 = [1,2,3]
data2 = [4,5,6,7]

result = generateSum(data1,data2)
print 'reuslt:',result
print my_quick_sort.run(result,0,len(result)-1,2)

