#coding:utf-8
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

# 已知两个单链表pHead1 和pHead2 各自有序，把它们合并成一个链表依然有序 
def merge(root1,root2):
	if root1 is None:return root2
	if root2 is None:return root1
	node = None
	if root1.val > root2.val:
		node = root2
		root2 = root2.next
	else:
		node = root1
		root1 = root1.next
	newRoot = node

	while not root1 is None and not root2 is None:

		if root1.val > root2.val:
			node.next = root2
			node = node.next
			root2 = root2.next
		else:
			node.next = root1
			node = node.next
			root1 = root1.next
	if root1 is None:
		node.next = root2
	if root2 is None:
		node.next = root1
	return newRoot

root1 = ListNode(1)
root1.next = ListNode(5)
root1.next.next = ListNode(7)

root2 = ListNode(3)
root2.next = ListNode(8)

newRoot = merge(root1,root2)
print newRoot.val
print newRoot.next.val
print newRoot.next.next.val
print newRoot.next.next.next.val
print newRoot.next.next.next.next.val
