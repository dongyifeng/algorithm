#coding:utf-8

class ListNode:
	def __init__(self,val):
		self.val = val
		self.next = None

def intersect(root1,root2):
	if root1 is None or root2 is None:return False
	node1 = root1
	node2 = root2
	while node1.next is not None or node2.next is not None:
		if node1.next is not None:
			print node1.val,"aaa"
			node1 = node1.next
		if node2.next is not None:
			print node2.val,"bbb"
			node2 = node2.next
	return node1 == node2
root1 = ListNode(1)
root1.next = ListNode(2)
root1.next.next = ListNode(3)
root1.next.next.next = ListNode(4)
root1.next.next.next.next = ListNode(5)

root2 = ListNode(7)
root2.next = ListNode(8)
root2.next.next = root1.next.next.next

print intersect(root1,root2)
print "-----------"
root3 = ListNode(10)
root3.next=root1.next.next.next.next
print intersect(root1,root3)
