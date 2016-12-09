#coding:utf-8
# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None
# 求单链表中结点的个数
def getListNodeCount(root):
	if root is None:return 0
	c = 0
	node = root
	while not node is None:
		node = node.next
		c +=1
	return c

root = ListNode(1)
root.next = ListNode(2)
root.next.next = ListNode(3)

print getListNodeCount(root)
