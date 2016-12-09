#coding:utf-8

# 求二叉树最小深度（最小深度：从根节点到叶子节点经过的节点）
# 注意：一棵树只有左节点，没有右节点，那么最小深度为2。

class TreeNode:
	def __init__(self,data,parent):
		self.data = data
		self.parent = parent
		self.left = None
		self.right = None

def minDepth(root):
	if root == None:return 0
	if root.left is not None:
		if root.right is not None:
			return min( minDepth(root.left),minDepth(root.right) ) + 1
		return minDepth(root.left) + 1
	elif root.right is not None:
		return minDepth(root.right) + 1
	return 1



tree = TreeNode(1,None)
tree.left = TreeNode(2,tree)
tree.right = TreeNode(3,tree)

tree.left.left = TreeNode(4,tree.left)
tree.left.right = TreeNode(5,tree.left)

tree.right.left = TreeNode(6,tree.right)

print minDepth(tree)

tree = TreeNode(1,None)
tree.right = TreeNode(3,tree)
print minDepth(tree)
