#coding:utf-8

def reverseString(s,f,t):
	while f < t:
		swap(s,f,t)
		f+=1
		t-=1
def leftRotateString(s,m):
	n = len(s)
	m %= n
	reverseString(s,0,m-1)
	reverseString(s,m,n-1)
	reverseString(s,0,n-1)

def swap(data,i,j):
	tmp = data[i]
	data[i]=data[j]
	data[j]=tmp


s = ['a5','a6','a7','b1','b2','b3','b4']
print s
#reverseString(s,0,3)
leftRotateString(s,3)
print s




