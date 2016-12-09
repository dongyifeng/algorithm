#coding:utf-8

# 求从数组a[1..n]中任选m个元素的所有组合。
# a[1..n]表示候选集，n为候选集大小，n>=m>0。
# b[1..M]用来存储当前组合中的元素(这里存储的是元素下标)
# 递归实现
def combine(a,n,m,b):
	for i in range(n,m-1,-1):
		b[m-1] = i-1
		if m > 1:
			combine(a,i-1,m-1,b)
		else:
			for j in range(len(b)-1,-1,-1):
				print a[b[j]],
			print ","


a=[1,2,3,4,5]
b=[0,0,0]
n = len(a)
m = len(b)
combine(a,n,m,b)

def combine(n,m):
	p = [0 for i in range(n)]
	data = [i for i in range(1,n+1)]
	for i in range(m):
		p[i] = 1
		print data[i],
	print ","
	while not isCompelet(p,m) :
		last = 0
		for i in range(n):
			t = p[i]
			if p[i] == 0 and last == 1:
				p[i-1] = 0
				p[i] = 1
				k = 0
				for j in range(i):
					if p[j] == 1:
						p[j] = 0
						p[k] = 1
						k += 1		
				break
			
			last = t
		#break
		for i in range(n):
			if p[i] == 1:
				print data[i],
		print ","			
		print p,isCompelet(p,m)


def isCompelet(data,m):
	for i in range(len(data)-1,m-2,-1):
#		print 'isCompelet',data[i],i
		if data[i] == 0:
			return False
	return True

n = 5
m = 3
print "--------------"
combine(n,m)

print "aaaaaaaaaaaaaaa"
p = [1, 0, 0, 1, 1]
print isCompelet(p,3)
