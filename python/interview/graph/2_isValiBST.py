# coding:utf-8
# 判断二叉搜索树 Leetcode 114
# 如果是二叉搜索树，中序遍历的结果是有序的。
# 但是我们没有必要将遍历结果存下来，再判断是否有序。在中序遍历时与前一个值比较一下就可以了（升序）。
# 中序遍历：left,root,right


class TreeNode:
	def __init__(self,val):
		self.val = val
		self.left = None
		self.right = None

def help(root,height):

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
