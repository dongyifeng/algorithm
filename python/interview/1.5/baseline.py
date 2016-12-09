
def longestPalindrome(a):
	if a is None:return 0
	n = len(a)
	result = 0
	c = 0
	# i is the middle point of the pallindrome
	for i in range(0,n):
		j = 0
		# if the length of the palindrome is odd
		while i >= j and i + j < n:
			if a[i-j] != a[i+j]:
				break
			c = j * 2 + 1
			j +=1 
		
		if c > result:
			result = c
		j = 0
		# for the even case
		while i >= j and i + j + 1 < n:
			if a[i - j] != a[i + j + 1]:
				break
			c = j * 2 + 2
			j += 1
		if c > result:
			result = c
	return result
a = 'abcdeffedcbauuuefeuue'
print longestPalindrome(a)
a = 'abcdefwfedcbauuuefeuue'
print longestPalindrome(a)
a = 'abc'
print longestPalindrome(a)
a = 'ecaacf'
print longestPalindrome(a)
