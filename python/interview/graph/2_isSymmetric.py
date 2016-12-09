#coding:utf-8

# 判断二叉树是否对称

class TreeNode:
	def __init__(self,val):
		self.val = val
		self.left = None
		self.right = None

def help(root1,root2):
	if root1 is None:
		return root2 is None
	if root2 is None:
		return False
	return root1.val == root2.val and help(root1.left,root2.right) and help(root1.right,root2.left)

def isSymmetric(root):
	if root is None:return True
	return help(root.left,root.right)

tree = TreeNode(1)
tree.left = TreeNode(2)
tree.right = TreeNode(3)

tree.left.left = TreeNode(4)
tree.left.right = TreeNode(5)

tree.right.left = TreeNode(6)
tree.right.right = TreeNode(7)
print isSymmetric(tree)


tree = TreeNode(1)
tree.left = TreeNode(2)
tree.right = TreeNode(2)

tree.left.left = TreeNode(4)
tree.left.right = TreeNode(5)

tree.right.left = TreeNode(5)
tree.right.right = TreeNode(4)
print isSymmetric(tree)




