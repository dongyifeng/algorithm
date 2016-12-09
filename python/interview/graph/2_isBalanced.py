#coding:utf-8
# 判断二叉树是否平衡二叉平衡树。
# 如果左子树不平衡，则不平衡
# 如果右子树不平衡，则不平衡
# 如果左右子树高度不同，则不平衡，否则平衡
# Leetcode 110

class TreeNode:
	def __init__(self,val):
		self.val = val
		self.left = None
		self.right = None

def help(root,height):
	if root is None:return (True,0)
	# 判断左子树是否平衡
	(balance,height1) = help(root.left,height)
	if not balance:return (False,height)
	# 判断右子树是否平衡
	(balance,height2) = help(root.right,height)
	if not balance:return (False,height)
	height = max(height1,height2) + 1
	if height1 == height2:
		return (True,height1+1)
	return (False,max(height1,height2)+1)

def isBalance(root):
	return help(root,0)[0]

tree = TreeNode(1)
tree.left = TreeNode(2)
tree.right = TreeNode(3)

tree.left.left = TreeNode(4)
tree.left.right = TreeNode(5)

tree.right.left = TreeNode(6)
tree.right.right = TreeNode(7)
print isBalance(tree)


tree = TreeNode(1)
tree.left = TreeNode(2)
tree.right = TreeNode(3)

tree.left.left = TreeNode(4)
tree.left.left.left = TreeNode(5)

print isBalance(tree)


	
