#coding:utf-8
# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

def tailK(root,k):
	if root is None or k <= 0:return None
	c = 0
	node = root
	while not node is None:
		node = node.next
		c += 1
	if c < k:return None
	sub = c - k + 1
	i = 0
	node = root
	while not node is None:
		i += 1
		if i == sub:return node
		node = node.next
	return None

root = ListNode(1)
root.next = ListNode(2)
root.next.next = ListNode(3)
root.next.next.next = ListNode(4)

print tailK(root,1).val
print tailK(root,4).val
print tailK(root,5).val
