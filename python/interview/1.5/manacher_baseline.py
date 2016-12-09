#coding:utf-8

def longest(s):
	if s is None or len(s) == 0:return
	mx = 1
	n = len(s)
	index = 0
	for i in range(1,n):
		j = k = i
		tmp = 0
		while j >= 0 and k < n:
			if s[j] != s[k]:
				break
			j -= 1
			k += 1
			tmp += 1
		if tmp > mx:
			mx = tmp
			index = i
	return mx-1,index

a = '#4#2#1#2#2#'
print a
print longest(a)

a = '42122'
def handle(s):
	n = len(s)
	r = [ '#' for i in range(( 2*n - 1 )) ]
	for i in range(n):
		r[ 2 * i ] = s[i]
	return r

print handle(a)
