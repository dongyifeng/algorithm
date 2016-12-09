#coding:utf-8
import math

# 完美洗牌

def swap(data,i,j):
	t = data[i]
	data[i] = data[j]
	data[j] = t

def cycleader(data,s,n,frist):
	first = 1
	while True:
		swap(data,s-1,first-1)
		first = (2*first)% (n +1)
		if first == s:
			break
# 数组从start 反转到 end
def reverse(data,start,end):
	while start < end:
		swap(data,start,end)
		start += 1
		end -= 1

# 循环右移num 位，时间复杂度O(n)
def leftRoteate(data,s,num,n):
	reverse(data,s,s+num-1)
	reverse(data,s+num,n)
	reverse(data,s,n)

def run(data,s,n):
	m = int(math.log(n+1,3))*2
	if m < n:
		count = (n/2)-m
		print m,count,n-count-1
		leftRoteate(data,m,count,n-count-1)
	print 's',data,s,m
	cycleader(data,s,2*m)
	#if 2*m < n:
	#	run(data,m+1,m+n/2)

#data =['a1','a2','a3','a4','a5','a6','a7','b1','b2','b3','b4','b5','b6','b7']
#cycleader(data,1,len(data))
data =['a1','a2','a3','a4','b1','b2','b3','b4']
print data
#leftRoteate(data,4,3,10)
cycleader(data,1,8,1)
print data
cycleader(data,1,8,3)
print data



#v2.leftRotateString(data,3)
#print data
