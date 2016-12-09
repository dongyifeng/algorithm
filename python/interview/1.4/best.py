#coding:utf-8

# 从中间向两端
def isPalindrome(a):
	if a is None:return None
	n = len(a)
	i = int(n / 2) - 1
	j = int(n / 2)
	if n % 2 != 0:
		j += 1 
	while i >= 0 and j < n :
		if a[i] != a[j]:
			return False
		i -= 1
		j += 1
	return True

a = 'acebeca'
print isPalindrome(a)

a = 'aceeca'
print isPalindrome(a)

a = 'abc'
print isPalindrome(a)
