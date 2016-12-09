#coding:utf-8

# 前缀和的应用
# 给定浮点数组a，求一个数组b，b[i] = a[0]*a[1]*..*a[i-1]*a[i+1]*..*a[n-1],不能使用除法，不允许再开数组。
# 关于前缀和的性质
# a[i] + a[i+1] + ... + a[j] = sum[j] - sum[i-1]

# 使用除法
def run(a):
	r = 1
	b =[]
	for item in a:
		r *= item
	for i in range(len(a)):
		b.append(r/a[i])
	return b

# 不使用除法
# 分析：先求“后缀积”
# 顺带求“前缀积”
def run2(a):
	n = len(a)
	b = [0 for i in range(n)]
	b[n-1] = 1
	for i in range(n-2,-1,-1):
		b[i] = b[i+1]*a[i+1]
	j = 1
	for i in range(n-1):
		j = j * a[i]
		b[i+1] = j * b[i+1]
		 
	return b
		


a = [2,2,3,4,5]
print a
b = run(a)
print b
a = [2,2,3,4,5]
print a
b = run2(a)
print '2',b


# 思考题
# 求数组中连续一段和，绝对值最小
# 提示：用前缀和排序

import sys

def run3(a):
	n = len(a)
	suffixSum = [0 for i in range(n)]
	suffixSum[0] = a[0]
	for i in range(1,n):
		suffixSum[i] = suffixSum[i-1] + a[i]
	print suffixSum
	r = sys.maxsize
	for i in range(0,n):
		for j in range(i+1,n):
			tmp = abs(suffixSum[i] - suffixSum[j])
			if tmp < r:
				r = tmp
	return r		

a = [1,2,-1,-2,5,-2,-1,7,6]
print a
print run3(a)

# 将一个数组从中间p位置分开，使得a[0] + ... + a[p-1] 与 a[p] + a[p+1] + ... + a[n-1] 差值最小
# 提示：前缀和，与总和减去前缀和的差最小，枚举
# 如果都是非负数，可以采取“两头扫”的方法，和较小的那边多加一个数


