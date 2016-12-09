#coding:utf-8

# 支持查询最小值的堆栈

import sys

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

class StackWrapper3:
	def __init__(self):
		self.stack1 = Stack()
		self.stack2 = Stack()
	def push(self,d):
		self.stack1.push(d)
	def pop(self):
		return self.stack1.pop()
	def getMin(self):
		print "pre",self.stack1.data
		r = sys.maxsize
		for i in range(self.stack1.size()):
			t = self.stack1.pop()
			if r > t:
				r = t
			self.stack2.push(t)
		for i in range(self.stack2.size()):
			self.stack1.push(self.stack2.pop())
		print "suffix",self.stack1.data
		return r

class StackWrapper2:
	def __init__(self):
		self.stack1 = Stack()
		self.stack2 = Stack()
	def push(self,d):
		self.stack1.push(d)
		if self.stack2.size() != 0 and self.stack2.top() < d:
			self.stack2.push(self.stack2.top())
		else:
			self.stack2.push(d)
	def pop(self):
		self.stack2.pop()
		return self.stack1.pop()
	def getMin(self):
		print "getMin1",self.stack1.data
		print "getMin2",self.stack2.data
		return self.stack2.top()

# s2 真的需要存那么多值么？假设s2之前入过的一个最小值，s2的top 端存了许多相同的最小值
class StackWrapper:
	def __init__(self):
		self.stack1 = Stack()
		self.stack2 = Stack()
	def push(self,d):
		self.stack1.push(d)
		if self.stack2.size() == 0 or self.stack2.top() >= d:
			self.stack2.push(d)
	def pop(self):
		print "pop1",self.stack1.data
		print "pop2",self.stack2.data
		if self.stack1.top() == self.stack2.top():
			self.stack2.pop()
		return self.stack1.pop()
	def getMin(self):
		print "getMin1",self.stack1.data
		print "getMin2",self.stack2.data
		return self.stack2.top()
	

stack = StackWrapper()
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(1)

print stack.pop()
print stack.getMin()

print "-"*50
stack = StackWrapper2()
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(1)

print stack.pop()
print stack.getMin()



print "-"*50
stack = StackWrapper3()
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(1)

print stack.pop()
print stack.getMin()
