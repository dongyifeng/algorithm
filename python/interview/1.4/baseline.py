#coding:utf-8

# 从两边向中间
def isPalindrome(a):
	if a is None:return None
	i = 0
	j = len(a) - 1 
	while i < j :
		if a[i] != a[j]:
			return False
		i += 1
		j -= 1
	return True

a = 'acebeca'
print isPalindrome(a)

a = 'aceeca'
print isPalindrome(a)

a = 'abc'
print isPalindrome(a)

a = 'google'
print isPalindrome(a)

