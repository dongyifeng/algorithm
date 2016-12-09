#coding:utf-8
# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None
#将单链表反转
def reverse(root):
	if root is None or root.next is None:return root
	node = root
	newListNode = None
	while not node is None:
		tmp = node
		node = node.next
		# 将当前结点摘下，插入新链表的最前端
		tmp.next = newListNode
		newListNode = tmp
	return newListNode

def reverse2(head):
	if head is None or head.next is None:return head
	result = None
	while head is not None:
		# 保存下一个节点
		tmp = head.next
		# 当前节点放到结果的开头
		head.next = result
		# 当前节点的头
		result = head
		# head 指向下一个节点
		head = tmp
	return result
		

root = ListNode(1)
root.next = ListNode(2)
root.next.next = ListNode(3)
#newListNode = reverse(root)
newListNode = reverse2(root)
print newListNode.val
print newListNode.next.val
print newListNode.next.next.val

# 思考题：
# 反转部分链表（m,n）之间反转。leetcode 92
# 在m 和n 处断开链表，反转m,n 之间的链表，最后再拼接到一起。

# leetcode 25
# 每k个元素反转一次
