#coding:utf-8
# leetcode 41

# 给一个数组，找到从1开始第一个不在里面的正整数（最大正整数为n）。
# [3,4,-1,1] 输出2
# 分析：让a[i] = i + 1
# 从0到i都满足a[i] = i + 1
# 对于 a[i] < i or a[i] > n or a[a[i]-1] = a[i] (重复)，删除这些无用的数据。

def swap(a,i):
	tmp = a[i]
	a[i] = a[tmp-1]
	a[tmp-1] = tmp

def run(a):
	n = len(a)
	i = 0
	while i < n:
		if a[i] == (i + 1):
			i += 1
		# 将最后一个数覆盖a[i],n-=1。删除a[i]
		if a[i] < i or a[i] > n or a[a[i]-1] == a[i]:
			n -= 1
			a[i] = a[n]
		# 交换位置，使a[i] = i + 1
		else:
			swap(a,i)
	# 排到第一个不连续的位置
	return n + 1


a =[3,4,-1,1]
print a
print run(a)
print a
