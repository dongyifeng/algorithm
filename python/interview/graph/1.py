#coding:utf-8

# 给定二叉树前中序遍历构造二叉

class TreeNode:
	def __init__(self,data,parent):
		self.data = data
		self.parent = parent
		self.left = None
		self.right = None

# 前序遍历
def preOrder(node):
	if node is None :return
	print node.data,
	preOrder(node.left)
	preOrder(node.right)

# 中序遍历
def middleOrder(node):
	if node is None:return
	middleOrder(node.left)
	print node.data,
	middleOrder(node.right)

# 后续遍历
def postOrder(node):
	if node is None:return
	postOrder(node.left)
	postOrder(node.right)
	print node.data,


tree = TreeNode(1,None)
tree.left = TreeNode(2,tree)
tree.right = TreeNode(3,tree)

tree.left.left = TreeNode(4,tree.left)
tree.left.right = TreeNode(5,tree.left)

tree.right.left = TreeNode(6,tree.right)
tree.right.right = TreeNode(7,tree.right)

print '----前序遍历----'
preOrder(tree)
print '\n----中序遍历----'
middleOrder(tree)
print '\n----后序遍历----'
postOrder(tree)
