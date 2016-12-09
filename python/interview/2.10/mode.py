#coding:utf-8

# 众数问题。
# 找出超过一半的数
# 分析：众数出现的次数大于其他所有数出现次数之和。
# 如果每次扔掉两个不同的数，最后剩下的就是众数。

def run(data):
	count = 0
	x = None
	for i in range(len(data)):
		# 表示x 已经扔干净了，所以需要重新找新的x
		if count == 0:
			x = a[i]
			count = 1
		# 如果x 与 a[i] 相等，count += 1 相当于不处理。
		elif x == a[i]:
			count += 1
		# 如果不相等，a[i] 扔掉就是i的自增，x 扔掉一个就是count -= 1
		else:
			count -= 1
	return x

a = [3,3,1,1,2,1,1,3,1,4,1,5,1]
print a
print run(a)

a = [1,1,2,3,4,5,6]
print a
print run(a)

# 扩展如何查找出现次数大于1/k 的数。
def run(data,k):
	kCount = {}
	kItem = {}
	for i in range(len(data)):
		if len(kCount) <=2 and kCount.get(data[i],0) == 0:
			kCount[data[i]] = 1
			kItem[data[i]] = 1
		elif 
	
