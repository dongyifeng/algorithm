#coding:utf-8

# 给出一单链表头指针pHead和一节点指针pToBeDeleted，O(1)时间复杂度删除节点pToBeDeleted
# 对于删除节点，我们普通的思路就是让该节点的前一个节点指向该节点的下一个节点，这种情况需要遍历找到该节点的前一个节点，时间复杂度为O(n)。对于链表，链表中的每个节点结构都是一样的，所以我们可以把该节点的下一个节点的数据复制到该节点，然后删除下一个节点即可。要注意最后一个节点的情况，这个时候只能用常见的方法来操作，先找到前一个节点，但总体的平均时间复杂度还是O(1)

class ListNode:
	def __init__(self,val):
		self.val = val
		self.next = None

def delete(root,node):
	if root is None or node is None:return
	if node.next is not None:
		node.val = node.next.val
		node.next = node.next.next
	# 要删除最后一个节点
	else:
		if root == node:
			root = None
		else:
			tmp = root
			while tmp != node:
				tmp = tmp.next
			tmp.next = None

root = ListNode(1)
root.next = ListNode(2)
root.next.next = ListNode(3)
root.next.next.next = ListNode(4)

delete(root,root)
print root.val
print root.next.val
print root.next.next.val
	
