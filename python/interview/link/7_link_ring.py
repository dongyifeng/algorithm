#coding:utf-8

class ListNode:
	def __init__(self,val):
		self.val = val
		self.next = None

# 判断一个单链表中是否有环
# 这里也是用到两个指针。如果一个链表中有环，也就是说用一个指针去遍历，是永远走不到头的。因此，我们可以用两个指针去遍历，一个指针一次走两步，一个指针一次走一步，如果有环，两个指针肯定会在环中相遇。时间复杂度为O（n）
def containsRing(root):
	if root is None:return False
	fast = root
	slow = root
	while fast is not None and slow is not None:
		fast = fast.next.next
		slow = slow.next
		if fast == slow:
			return True
	return False

root = ListNode(1)
root.next = ListNode(2)
root.next.next = ListNode(3)
root.next.next.next = ListNode(4)
root.next.next.next.next = ListNode(5)
root.next.next.next.next.next = ListNode(6)
root.next.next.next.next.next.next =  root.next.next.next

print containsRing(root)

root1 = ListNode(1)
root1.next = ListNode(2)
root1.next.next = ListNode(3)
root1.next.next.next = ListNode(4)
root1.next.next.next.next = ListNode(5)
root1.next.next.next.next.next = ListNode(6)
print containsRing(root1)
