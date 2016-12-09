#coding:utf-8
#在二元树中找出和为某一值的所有路径 输入一个整数和一棵二元树，从树的根结点开始往下访问一直到叶结点所经过的所有结点形成一条路径，然后打印出和与输入整数相等的所有路径。 例如输入整数22和如下二元树
#			10
#		5		12
#	    4	   7
#则打印出两条路径：10, 12和10, 5, 7


class binaryTreeNode:
	def __init__(self,value,left,right,parent):
		self.value = value
		self.left = left
		self.right = right
		self.parent = parent

def leafNodeToRootNode(leafNode):
	if leafNode is None:return
	print leafNode.value
	leafNodeToRootNode(leafNode.parent)
	

def run(binaryTree,k,s):
	s += binaryTree.value
	if binaryTree.left is None and binaryTree.right is None:
		if k == s:
			leafNodeToRootNode(binaryTree)
			print '-'*10
	else:
		if s < k:
			if not binaryTree.left is None:
				run(binaryTree.left,k,s)
			if not binaryTree.right is None:
				run(binaryTree.right,k,s)

data = [10,5,12,4,7]

root = binaryTreeNode(10,None,None,None)
left = binaryTreeNode(5,None,None,root)
right = binaryTreeNode(12,None,None,root)
root.left = left
root.right = right

left_left = binaryTreeNode(4,None,None,left)
left_right = binaryTreeNode(7,None,None,left)

left.left = left_left
left.right = left_right

run(root,22,0)
