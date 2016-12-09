#coding:utf-8

class ListNode:
	def __init__(self,val):
		self.val = val
		self.next = None

# 已知一个单链表中存在环，求进入环中的第一个节点
# 首先判断是否存在环，若不存在结束。在环中的一个节点处断开（当然函数结束时不能破坏原链表），这样就形成了两个相交的单链表，求进入环中的第一个节点也就转换成了求两个单链表相交的第一个节点。
# 1 --> 2 --> 3 --> 4 --> 5 
#		    |	  |
#	            7 <---6
# 判断是否有环 在 5 节点判断,将5作为tail，分为1 --> 2 --> 3 --> 4 --> 5 和 6 --> 7 --> 4 --> 5 队列的第一个交点问题。

def getFirstNodeInCircle(root):
	if root is None:return None
	fast = root
	slow = root
	while fast is not None and slow is not None:
		fast = fast.next.next
		slow = slow.next
		if fast == slow:
			break
	if fast is None or slow is None:
		return None
	newTail = slow
	node1 = root
	node2 = newTail.next
	len1 = len2 = 1
	while node1 != newTail:
		node1 = node1.next
		len1 += 1
	while node2 != newTail:
		node2 = node2.next
		len2 += 1
	node1 = root
	node2 = newTail.next
	if len1 > len2:
		k = len1 - len2
		while k > 0:
			node1 = node1.next
			k -= 1
	else:
		k = len2 - len1
		while k > 0:
			node2 = node2.next
			k -= 1
	while node1 != node2:
		node1 = node1.next
		node2 = node2.next
	return node1
# n 圈长
# 起点到圈的起点距离为a
# slow 到圈起点时，p2在权重的位置。
# slow 到圈起点后，与fast 相距 n - x 步（追击问题）。
# 设相遇点到圈起点距离是b
# slow 走的距离是 a + b
# fast 走的距离是 a + b + k*n (k 圈)
# 由于fast 速度是slow 的2 倍：a + b + k*n = 2*(a + b)
# a + b = k*n ; a + b 是圈长的整数倍
# 根据上边的结论：找圈的起点。
# fast 与 slow 相遇后，我们将slow 拉回链表起点，fast 继续从相遇点走。a 步后，slow 到圈起点，fast 也刚好到圈起点。
# a = k*n - b ; 因为fast 距离起点已经走了b 了。 
# 如何确定圈长？
# 相遇后，fast 再走一圈并统计长度就是圈长
 

def detectCycle(head):
	fast = head
	slow = head
	while fast is not None and slow is not None:
		fast = fast.next.next
		slow = slow.next
		if fast == slow:
			break
	if fast is None or slow is None:
		return None
	
	slow = head
	while True:
		slow = slow.next
		fast = fast.next
		if fast == slow:
			break
	return slow


root = ListNode(1)
root.next = ListNode(2)
root.next.next = ListNode(3)
root.next.next.next = ListNode(4)
root.next.next.next.next = ListNode(5)
root.next.next.next.next.next = ListNode(6)
root.next.next.next.next.next.next = ListNode(7)
root.next.next.next.next.next.next.next =  root.next.next.next

#print getFirstNodeInCircle(root).val
print detectCycle(root).val
