#coding:utf-8

def swap(data,i,j):
	tmp = data[i]
	data[i] = data[j]
	data[j] = tmp

def calcAllPermutation(data,s,e):
	if e <=1:return
	if s == e:
		for i in range(e):
			print data[i],
		print
	else:
		for j in range(s,e):
			swap(data,j,s)
			calcAllPermutation(data,s + 1,e)
			# 为了将上边swap 转换的数据，转换回来，为下一组准备。A B C | B A C | C B A ,使都是在原数组上将每一位替换到第一位，同时也保证了在计算完毕全排后，原来data顺序没有改变。
			swap(data,j,s)

def reverse(data,begin,end):
	while begin < end:
		swap(data,begin,end)
		begin += 1
		end -= 1
# 下一个排列
# (1, 2, 3, 4)
# (1, 2, 4, 3)
# ...
# (1, 4, 2, 3)
# (1, 4, 3, 2)
# 输入(1, 2, 3, 4) 输出(1, 2, 4, 3)；输入：(1, 4, 2, 3) 输出 (1, 4, 3, 2)；输入(4, 3, 2, 1)，输出：(1, 2, 3, 4)
# 方法：二找，一交换，一翻转
def nextPermutation(data):
	n = len(data)
	x = n - 2
	# 从后向前严格升序
	while x >= 0 and data[x] >= data[x+1]:
		x -= 1
	# 输入是最后一个排序，特殊情况
	if x < 0:
		reverse(data,0,n-1)
		return
	y = n - 1
	# data[x] 后的数都是降序，从后向前找到第一个大于data[x] 的位置
	while data[y] <= data[x]:
		y -= 1

	print "x:",x,"y:",y,"data[x]",data[x],"data[y]",data[y]
	swap(data,x,y)
	# 交换后a[x+1,n-1]仍然是降序
	# 逆转等于排序
	reverse(data,x+1,n-1)
	
def prePernutation(data):
	n = len(data)
	x = n - 2
	while x >= 0 and data[x] <= data[x+1]:
		x -= 1
	if x < 0:
		reverse(data,0,n-1)
		return
	y = n - 1
	while data[y] >= data[x]:
		y -= 1
	swap(data,x,y)
	reverse(data,x+1,n-1)
data = ['SUPER_VIP','VIP','ORDINARY','SUB']
#data = [1,2,3,4]
calcAllPermutation(data,0,len(data))

data = ['VIP','ORDINARY','SUB']
calcAllPermutation(data,0,len(data))




data = [2, 5, 4, 3, 1, 0]
print data
nextPermutation(data)
print "nextPermutation:",data

print "-"*100
data = [2, 5, 4, 3, 1, 0]
print data
prePernutation(data)
print 'end',data
