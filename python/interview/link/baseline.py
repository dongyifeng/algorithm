# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = None
        lastNode = None
        tmp1 = l1
        tmp2 = l2
        nextVal = 0
        while not tmp1 is None and not tmp2 is None:
            sums = nextVal + tmp1.val + tmp2.val
            node = ListNode(sums % 10 )
            print sums,tmp1.val,tmp2.val
            if head is None:
                head = node
            if not lastNode is None:
                lastNode.next = node
            lastNode = node
            nextVal = int(sums / 10)
            tmp1 = tmp1.next
            tmp2 = tmp2.next
            
        return head

l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

r = Solution().addTwoNumbers(l1,l2)
print 'r',r.val
print 'r',r.next.val
print 'r',r.next.next.val
