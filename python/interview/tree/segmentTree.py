#coding:utf-8

# 线段树
# http://zhikaizhang.cn/2016/05/08/%E6%95%B0%E6%8D%AE%E7%BB%93%E6%9E%84%E4%B9%8B%E7%BA%BF%E6%AE%B5%E6%A0%91/
# 使用线段树可以快速的查找某一个索引或某个索引的区间，时间复杂度为O(logn），空间复杂度为O(n)

class Node:
	def __init__(self,start,end,value):
		self.start = start
		self.end = end
		self.value = value
		self.left = None
		self.right = None

class SegmentTree:
	def __init__(self,data):
		if data is None or len(data) == 0:return
		self.root = self.build(data,0,len(data)-1)
	def query(self,start,end):
		return self.query(self.root,start,end)
	def modify(self,index,value):
		self.modify(self.root,index,value)
	def build(self,start,end,data):
		if start == end:
			return Node(start,end,A[start])
		cur = Node(start,end,0)
		# mid = start + ((end-start)>>1)
		mid = start + (end-start)/2
		cur.left = self.build(start,mid,data)
		cur.right = self.build(min+1,end,data)
		cur.value = cur.left.value + cur.right.value 
		return cur
	def query(self,node,start,end):
		# 查询与该区间完全吻合直接返回
		if start == node.start and end == node.end:
			return cur.value
		int mid = node.start + ((node.end-node.start)>>1)
		if start > mid:
			return self.query(node.right,start,end)
		if end < mid +1:
			return self.query(node.left,start,end)
		# 查询横跨左右子树，查询出两个子树的部分求和即可
		return self.query(node.left,start,end) + self.query(node.right,mid+1,end)
	def modify(self,node,index,value):
		# 该节点是叶子节点且是要修改的索引，则修改该节点value
		if node.start == index and node.end == index:
			node.value = value
			return
		mid = start + ((end - start)>>1)
		if index > mid:
			self.modify(node.right,index,value)
		else:
			self.modify(node.left,index,value)
		node.value = node.left.value + node.right.value


