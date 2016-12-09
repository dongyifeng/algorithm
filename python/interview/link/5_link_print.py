#coding:utf-8
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

# 从尾到头打印单链表
def printListNode(root):
	if root is None:return
	printListNode(root.next)
	print root.val

root1 = ListNode(1)
root1.next = ListNode(2)
root1.next.next = ListNode(3)
printListNode(root1)
