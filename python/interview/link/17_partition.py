#coding:utf-8

# 链表partition
# 链表里存放整数，给定x 把比x小的节点放到>= x 之前。Leetcode 86

# 于数组partition过程不一样，数组需要不断swap ，而链表,只需重新起一个链表，一个存 <= x ,另一个存 >= x 的。最后将两个链表重新连接起来。并没有使用的空间。

class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

def partition(head,k):
	l1 = None
	l2 = None
	node = head
	while node is not None:
		print 'while',node.val
		tmp = node.next
		node.next = None
		if node.val <= k:
			print "l1",node.val
			if l1 is None:
				l1 = node
			else:
				node.next = l1
				l1 = node
		else:
			print 'l2',node.val
			if l2 is None:
				l2 = node
			else:
				node.next = l2
				l2 = node
		node = tmp
	if l1 is None:
		return l2
	node = l1
	while node.next is not None:
		node = node.next	
	node.next = l2
	return l1


root = ListNode(4)
root.next = ListNode(7)
root.next.next = ListNode(2)
root.next.next.next = ListNode(50)
root.next.next.next.next = ListNode(1)
root.next.next.next.next.next = ListNode(30)
root.next.next.next.next.next.next = ListNode(20)
root.next.next.next.next.next.next.next = ListNode(10)

la = partition(root,4)
print la.val
print la.next.val
print la.next.next.val
print la.next.next.next.val
print la.next.next.next.next.val
print la.next.next.next.next.next.val
print la.next.next.next.next.next.next.val
print la.next.next.next.next.next.next.next.val
