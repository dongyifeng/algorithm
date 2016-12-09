#coding:utf-8

#解法一
#首先考虑最简单的情况。如果只有1级台阶，那显然只有一种跳法。如果有2级台阶，那就有两种跳的方法了：一种是分两次跳，每次跳1级；另外一种就是一次跳2级

def run(k):
	if k <= 2: return k
	return run(k-1) + run(k-2)
k = 5
print run(k)

# 如果一个人上台阶可以一次上1个，2个，或者3个呢？这个时候，公式是这样写的
def run(k):
	if k <= 2:return k
	if k == 3:return 4
	return run(k-1) + run(k-2) + run(k-3)

k = 8
print run(k)
