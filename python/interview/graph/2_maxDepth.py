#coding:utf-8

# 求二叉树最大深度

class TreeNode:
	def __init__(self,val):
		self.val = val
		self.left = None
		self.right = None

def maxDepth(root):
	if root == None:return 0
	return max( maxDepth(root.left),maxDepth(root.right) ) + 1

