
def leftShiftOne(s):
	f = s[0]
	n = len(s)
	for i in range(1,n):
		s[i-1]=s[i]
	s[n-1] = f

def leftRotateString(s,m):
	for i in range(0,m):
		leftShiftOne(s);

s = ['a','b','c','d','e']
print s
leftRotateString(s,2)
print s
