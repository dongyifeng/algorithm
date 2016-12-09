#coding:utf-8

# 单调堆栈——最大直方图

class Stack:
	def __init__(self):
		self.data = []
	def push(self,d):
		self.data.append(d)
	
	def pop(self):
		return self.data.pop()
	def size(self):
		return len(self.data)
	def top(self):
		return self.data[-1]

# [2,1,5,6,2,3]
# height[i] 以为中心点，向两边搜索，以比自己小的数为界，停止搜索，计算wide度。
# 这个办法没有使用额外的空间，但是有重复搜索。

def baseline(height):
	n = len(height)
	result = 0
	for i in range(n):
		k = i - 1
		j = i + 1
		wide = 1
		while True:
			if k >=0 and height[k] >= height[i]:
				wide += 1
				k -= 1
			elif j < n and height[j] >= height[i]:
				wide += 1
				j += 1
			else:
				break
		result = max(height[i] * wide,result)
	return result

# 借助一个堆栈，避免重复搜索。
# 我用了 eara 数组，存左边界，其实不需要，左边界就是s.top()
def myRun(height):
	n = len(height)
	result = 0
	s = Stack()
	aera = [None for i in range(n)]
	for i in range(n):
		# 出栈
		while s.size() != 0 and height[s.top()] >= height[i]:
			d = s.pop()
			a = (i - aera[d] - 1 ) * height[d]
			result = max(result,a)
		if s.size() == 0:
			left = -1
		else:
			left = s.top()
		s.push(i)
		aera[i] = left
	return result

# 在出栈时 i 就是右结界，s.pop() 是左结界。O(n) 可以解决。
def run(height):
	n = len(height)
	result = 0
	s = Stack()
	for i in range(n):
		while s.size() != 0 and height[s.top()] >= height[i]:
			d = s.pop()
			if s.size() == 0:
				left = -1
			else:
				left = s.top()
			a = (i - left - 1 ) * height[d]
			result = max(result,a)
		s.push(i)
#	while s.size() != 0:
#		h = height[s.top()]
#		s.pop()
#		if s.size() == 0:
#			left = -1
#		else:
#			left = s.top()
#		result = max(result,( n - 1 - left )*h)
	return result
	
height = [2,1,5,6,2,3]
print baseline(height)

print '-'*50

height = [2,1,5,6,2,3,0]
print myRun(height)

print '-'*50

height = [2,1,5,6,2,3,0]
print run(height)
