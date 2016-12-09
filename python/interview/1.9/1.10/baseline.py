#coding:utf-8

# 给定两个串 a 和 b ，问b 是否a 的子串的变位词。
# a = hello ,b=lel,lle 都是true 但是b=elo 是false。注意：子串是必须连续

# 分析
# 滑动窗口的思想。
# 动态维护一个“窗口”，比如len(b) == 3 ,窗口a[0..2],a[1..3],a[2..4]
# 如何比较窗口与b比较？
# 用一个hash，如果是小写英文字母，用[0..25]表示b中每个单词出现的次数。
# 关键：num 数组是a的窗口与b字符是否存在的差。
#       nonZero 表示num 中非零元素的个数，当nonZero == 0 时表示a的窗口与b 完全相等。注意：在num[i] =1 变为num[i] =2 是，不需要维护nonZero
# 由于动态维护num 和nonZero 所以，不需要每个新窗口都逐一比较

def run(a,b):
	if len(a) <= len(b):return False
	lenb = len(b)
	num = [0 for i in range(26)]
	origin = ord('a')
	nonZero = 0
	for i in range(lenb):
		c = ord(b[i])-origin
		num[c] += 1
		if num[c] == 1:
			nonZero += 1		
	# 第一个窗口
	for i in range(lenb):
		c = ord(a[i]) - origin
		num[c] -= 1
		if num[c] == 0:
			nonZero -= 1
		elif num[c] == -1:
			nonZero += 1
	if nonZero == 0:return True

	# 窗口滑动
	for i in range(lenb,len(a)):
		c = ord(a[i-lenb]) - origin
		num[c] += 1
		if num[c] == 0:nonZero -=1
		elif num[c] == -1:nonZero += 1

		c = ord(a[i]) - origin
		num[c] -= 1
		if num[c] == 0:nonZero -= 1
		elif num[c] == -1:nonZero +=1

		if nonZero == 0:return True
	return False

a = 'hello'
b = 'elo'
print "a",a,'b',b
print run(a,b)
