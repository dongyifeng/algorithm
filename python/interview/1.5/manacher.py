#coding:utf-8

def longestPalindrome(a):
	if a is None:return 0
	n = len(a)
	p = [ 0 for i in range(n) ]
	mx = 0
	id_int = 0
	for i in range(n):
		# j 是 i 关于id_int 的对称点
		j = 2 * id_int - i
		# i 在以 id_int 为中心点的palindrome 的范围内，初始化p[i],避免重复查找。
		if mx > i:
			p[i] = min(p[j],mx - i)
		else:
			p[i] = 1
		# 在p[i] 基础上查找以 i 为中心的palindrome
		while i >= p[i] and i + p[i] < n and a[i + p[i]] == a[i - p[i]]:
			p[i] += 1
		if i + p[i] > mx:
			mx = i + p[i]
			id_int = i
	print p
	return max(p) - 1
#a = '#1#2#2#1#2#3#2#1#'
a = '#4#2#1#2#2#'
print a
print longestPalindrome(a)
