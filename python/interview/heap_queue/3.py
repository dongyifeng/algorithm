#coding:utf-8

# 用两个堆栈实现一个队列

class Stack:
	def __init__(self):
		self.data = []
	def push(self,d):
		self.data.append(d)
	
	def pop(self):
		return self.data.pop()
	def size(self):
		return len(self.data)

class Queue:
	def __init__(self):
		self.stack1 = Stack()
		self.stack2 = Stack()
	def push(self,d):
		self.stack1.push(d)
	
	def pop(self):
		if self.stack2.size() > 0:
			return self.stack2.pop()
		for i in range(self.stack1.size()):
			self.stack2.push(self.stack1.pop())
		return self.stack2.pop()

	
queue = Queue()
queue.push(1)
queue.push(2)
queue.push(3)

print queue.pop()
queue.push(4)
print queue.pop()
queue.push(5)
print queue.pop()
print queue.pop()



