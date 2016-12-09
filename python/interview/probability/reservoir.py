#coding:utf-8

# 水库（Reservoir）采样
# 流入若干个对象（整数），事先不知道个数。如何随机取出k个（k小于总数）？
# 算法：用一个数组a保存k个数a[0...k-1]
# 对于第i个元素(i=1,2...)
# 	如果i<=k:则a[i-1]存放这个元素
#	否则：产生随机数x=rand()%i
#		若x<k,则用a[x]存在这个元素（扔掉之前的元素）

# 算法优点：不需要预先知道元素个数（可以一个一个流入）
# 证明：假设目前已经流入n>k 个元素
# 第i(i<=k)个元素被选中的可能性
#	1*k/(k+1)*(k+1)/(k+2)*...*(n-1)/n=k/n
# 第i(i>k)个元素被选中的可能性
# 	k/i * i(i+1) * (i+1)/(i+2)* ... * (n-1)/n = k/n

class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

import random
def run(head,k):
	result = [ None for i in range(k) ]
	i = 1
	node = head
	while node is not None:
		if i <= k:
			result[i-1] = node.val
		else:
			# 均匀产生0~i 之间的随机数
			x = random.randint(0,i)
			if x < k:
				result[x] = node.val
		i += 1
		node = node.next
	return result

# 思考与扩展
# k == 1 的特殊性
# 一个若干行的大文件，随机选择一行。
# 一个不知道长度的链表，随机选择一个或者多个元素
# 带全采样--如果每个元素权重不同，如何办？

# k == 1
def randomOne(head):
	result = None
	node = head
	i = 1
	while node is not None:
		if random.randint(0,i) == 1:
			result = node.val
		node = node.next
		i += 1
	return result


# 带全采样--如果每个元素权重不同，如何办？
# 给定n中元素，在给定n个权值，按权值的比例随机抽样一个元素，为了方便我们可以假设权值全是整数。
# 方法1:每个元素复制权值那么多份，用水库采样
#	例如：3个a，2个b，5个c
#		aaabbccccc
#	优点：可以使用已有方法
#	缺点：需要自己复制

# 方法2：每个元素按照权值对应一个区间
#	例如3个a，2个b，5个c
#	a对应[0...2],b对应[3..4],c对应[5..9]
#	随机产生一个[0..9]的随机数，二分查找最后对应的元素是哪一个
#	优点：省空间
#	缺点：需要二分查找

# 方法3：假设有m种元素
#	1.先按1/m的概率随机选择一种元素
#	2.*再产生随机数根据权值决定能否选择这种元素，如果能则选取它并结束，否则返回1
#		p_i_1 = W_i / W_total  (W_total = sum(W_i))
#	或者	p_i_2 = W_i / W_max 
#	用random.random() < p_i_1 ,要否则不要
#	用random.randint(1,b),是否小于等于W_i
#	用random.randint(0,b-1)是否小于W_i
# why
# 实验

def wRandomOne(data,frac):
	m = len(data)
	result = data[random.randint(0,m-1)]
	w_total = sum(frac)
	for i in range(m):
		if random.randint(0,w_total) < frac[i]:
			return data[i]
	return result

def wRandom(data,frac,k):
	return [ wRandomOne(data,frac) for i in range(k) ]	


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
head.next.next.next.next.next = ListNode(6)
head.next.next.next.next.next.next = ListNode(7)
head.next.next.next.next.next.next.next = ListNode(8)
head.next.next.next.next.next.next.next.next = ListNode(9)
head.next.next.next.next.next.next.next.next.next = ListNode(10)

k = 3
print run(head,k)
print randomOne(head)


data = ["a","b","c","d","e","f","g"]
frac = [1,200,100,80,70,30,50]
k = 1
print wRandomOne(data,frac)
print wRandom(data,frac,2)







			
	
	
