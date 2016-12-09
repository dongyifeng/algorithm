#coding:utf-8

# 单调队列——滑动窗口最大值 
# 给定一个数组a[0..n],还有一个值k，计算数组b[i]=max(a[i-k+1..i]),注意认为负数下标对应值是无穷小
# 方案一：维护一个k个数的最大堆;O(nlogk)

class Deque:
	def __init__(self):
		self.data = []
	def push(self,d):
		self.data.append(d)

	def popFront(self):
		return self.data.pop(0)

	def back(self):
		return self.data[-1]

	def popBack(self):
		return self.data.pop()	
	def front(self):
		return self.data[0]

	def size(self):
		return len(self.data)
	def clean(self):
		self.data = []

import sys

# 通过一个双端队列，维护两个数，一个最大值，一个次大值。
# stack.front() 总是最大值的下标。
# 注意：过期和仍队列都是循环，如果data[i] 比queue 中数都大，queue会被清空，清空后，在后边s.push(i),就是当前最大值
def run(data,k):
	n = len(data)
	s = Deque()
	b = [None for i in range(n)]
	for i in range(n):
		# 过期
		# 从前向后过期
		while s.size() != 0 and s.front() <= i - k:
			s.popFront()
		# 扔队尾
		# 从后向前扔
		while s.size() !=0 and data[s.back()] <= data[i]:
			s.popBack()
		s.push(i)
		b[i] = data[s.front()]
		print s.data
	return b

data = [2,1,5,3,4,2,6]
print data
print run(data,3)	


# 扩展：如果输入是一个流，我们必须自己保存“时间戳”，决定过期。
