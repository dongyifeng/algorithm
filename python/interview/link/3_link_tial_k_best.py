#coding:utf-8
# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

def tailK(root,k):
	if root is None or k <= 0:return None
	c = 0
	behind = root
	ahead = root
	while not ahead is None and k > 1:
		ahead = ahead.next
		k -= 1
	if k > 1 or ahead is None:return None
	while not ahead.next is None:
		ahead = ahead.next
		behind = behind.next
	return behind

root = ListNode(1)
root.next = ListNode(2)
root.next.next = ListNode(3)
root.next.next.next = ListNode(4)

print tailK(root,1).val
print tailK(root,4).val
print tailK(root,2).val
