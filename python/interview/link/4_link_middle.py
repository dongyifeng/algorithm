#coding:utf-8
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

# 查找单链表的中间结点
def getMiddleNode(root):
	if root is None or root.next is None:return root
	ahead = root
	behind = root
	while not ahead.next is None:
		ahead = ahead.next
		behind = behind.next
		if not ahead.next is None:
			ahead = ahead.next
	return behind

root1 = ListNode(1)
root1.next = ListNode(2)
root1.next.next = ListNode(3)

root2 = ListNode(1)
root2.next = ListNode(2)
root2.next.next = ListNode(3)
root2.next.next.next = ListNode(4)

print getMiddleNode(root1).val
print getMiddleNode(root2).val
