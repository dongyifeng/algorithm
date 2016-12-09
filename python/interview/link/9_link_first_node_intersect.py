#coding:utf-8

class ListNode:
	def __init__(self,val):
		self.val = val
		self.next = None
# 求两个单链表相交的第一个节点
# 对第一个链表遍历，计算长度len1，同时保存最后一个节点的地址。
#对第二个链表遍历，计算长度len2，同时检查最后一个节点是否和第一个链表的最后一个节点相同，若不相同，不相交，结束。
#两个链表均从头节点开始，假设len1大于len2，那么将第一个链表先遍历len1-len2个节点，此时两个链表当前节点到第一个相交节点的距离就相等了，然后一起向后遍历，知道两个节点的地址相同。
def getFirstIntersectNode(root1,root2):
	if root1 is None or root2 is None:return None
	node1 = root1
	node2 = root2
	len1 = len2 = 0
	while node1.next is not None or node2.next is not None:
		if node1.next is not None:
			node1 = node1.next
			len1 += 1
		if node2.next is not None:
			node2 = node2.next
			len2 += 1
	if node1 != node2:return None
	if len1 < len2:
		long_link = root2
		short_link = root1
		sub = len2 - len1
	else:
		long_link = root1
		short_link = root2
		sub = len1 - len2
	c = 0
	while long_link.next is not None:
		if c < sub:
			long_link = long_link.next
			c += 1
			continue
		if short_link == long_link:
			return long_link	
		long_link = long_link.next
		short_link = short_link.next
	

root1 = ListNode(1)
root1.next = ListNode(2)
root1.next.next = ListNode(3)
root1.next.next.next = ListNode(4)
root1.next.next.next.next = ListNode(5)

root2 = ListNode(7)
root2.next = ListNode(8)
root2.next.next = root1.next.next.next


print getFirstIntersectNode(root1,root2).val
