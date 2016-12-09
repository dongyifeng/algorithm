#coding:utf-8

# 二叉树转链表
# 思路：
# 1.左子树转成单链
# 2.右子树转成单链
# 3.将左链接到右链
# Leetcode 144

class TreeNode:
	def __init__(self,data,parent):
		self.data = data
		self.parent = parent
		self.left = None
		self.right = None

def help(root,last):
	last = root
	if root is None:return
	mylast = tmp = root.right
	help(root.left,mylast)
	if mylast is not None:
		last = mylast
		last.right = tmp
		root.right = root.left
		root.left = None
	help(tmp,mylast)
	if mylast is not None:
		last = mylast		
	
def flatten(root):
	last = None
	help(root,last)


# 链表转二叉树
# 方法1 O(nlogn)
# 1.求链表长度
# 2.链表不能随机访问。
# 如果是数组可以做成O(n)


# 方法2：O(n)
# 1.求链表长度


# 思考题：
# 数组转二查树 
