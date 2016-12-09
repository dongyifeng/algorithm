#coding:utf-8

# 用两个队列实现一个堆栈

class Queue:
	def __init__(self):
		self.data = []
	def push(self,d):
		self.data.append(d)
	
	def pop(self):
		return self.data.pop(0)
	def size(self):
		return len(self.data)

class Stack:
	def __init__(self):
		self.queue1 = Queue()
		self.queue2 = Queue()
	def push(self,d):
		if self.queue1.size() != 0:
			self.queue1.push(d)
		else:
			self.queue2.push(d)
	
	def pop(self):
		if self.queue1.size() != 0:
			for i in range(1,self.queue1.size()):
				self.queue2.push(self.queue1.pop())
			return self.queue1.pop();
		else:
			for i in range(1,self.queue2.size()):
				self.queue1.push(self.queue2.pop())
			return self.queue2.pop()

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)

print stack.pop()
print stack.pop()
print stack.pop()


