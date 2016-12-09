#coding:utf-8

# 二叉树每个节点有一个整数，返回和最大的路径

class TreeNode:
	def __init__(self,data,parent):
		self.data = data
		self.parent = parent
		self.left = None
		self.right = None

def help(root,m):
	if root is None:return (0,m)
	(left,m) = help(root.left,m) 
	(right,m) = help(root.right,m)
	ret = max(max(left,right),0) + root.data
	m = max(m,ret)
	return (ret,m)

def maxPathSum(root):
	if root is None:return 0
	result = root.data
	(tmp,result) = help(root,result)
	return result


tree = TreeNode(1,None)
tree.left = TreeNode(2,tree)
tree.right = TreeNode(3,tree)

tree.left.left = TreeNode(4,tree.left)
tree.left.right = TreeNode(5,tree.left)

tree.right.left = TreeNode(6,tree.right)
tree.right.right = TreeNode(7,tree.right)

print maxPathSum(tree)
