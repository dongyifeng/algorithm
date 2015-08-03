# coding:UTF-8
# 堆排序

class heap:
	def build(self,data):
		self.heapSize=len(data)
		self.data=data
		print self.left(5)
		for i in range(len(data)/2,0,-1):
			self.maxHeapify(i)
			print i,data
			print ""
	def left(self,i):
		if 2*i > self.heapSize:return None
		return self.data[2*i-1]
	def right(self,i):
		if 2*i+1 > self.heapSize:return None
		return self.data[2*i]
	def parent(self,i):
		return self.data[i/2]

	def maxHeapify(self,i):
		if i > self.heapSize/2:return
		left=self.left(i)
		right=self.right(i)
		largest=max(self.data[i-1],left,right)
		if largest==self.data[i-1]:
			return
		
		index= 2*i if largest==left else (2*i+1)
		exchange(self.data,i-1,index-1)
		self.maxHeapify(index)
	def sort(self):
		for i in range(len(self.data)-1,-1,-1):
			exchange(self.data,0,i)
			self.heapSize-=1
			self.maxHeapify(1)

def exchange(data,i,j):
	tmp=data[i]
	data[i]=data[j]
	data[j]=tmp

data=[4,1,3,2,16,9,10,14,8,7]
print data
print "start"
h= heap()
h.build(data)
print data
h.sort()
print "end"
print data
