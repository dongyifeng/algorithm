#coding:utf-8

# 判断两个二叉树是否相同

class TreeNode:
	def __init__(self,val):
		self.val = val
		self.left = None
		self.right = None

def isSameTree(root1,root2):
	if root1 is None:
		return root2 is None
	if root2 is None:
		return False
	return root1.val == root2.val and isSameTree(root1.left,root2.left) and isSameTree(root1.right,root2.right)	

tree = TreeNode(1)
tree.left = TreeNode(2)
tree.right = TreeNode(3)

tree.left.left = TreeNode(4)
tree.left.right = TreeNode(5)

tree.right.left = TreeNode(6)
tree.right.right = TreeNode(7)


tree1 = TreeNode(1)
tree1.left = TreeNode(2)
tree1.right = TreeNode(3)

tree1.left.left = TreeNode(4)
tree1.left.right = TreeNode(5)
tree1.right.left = TreeNode(6)
tree1.right.right = TreeNode(7)
print isSameTree(tree,tree1)


tree1 = TreeNode(1)
tree1.left = TreeNode(2)
tree1.right = TreeNode(3)

tree1.left.left = TreeNode(4)
tree1.left.right = TreeNode(5)
tree1.right.left = TreeNode(6)
print isSameTree(tree,tree1)

