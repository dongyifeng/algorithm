#coding:utf-8

# 朴素递归实现O(n^3)
def editDistance(src,dest):
	print "first"
	if len(src) == 0 or len(dest) == 0:
		return abs(len(src) - len(dest))
	if src[0] == dest[0]:
		return editDistance(src[1:],dest[1:])
	edInsert = editDistance(src,dest[1:]) + 1
	edDelete = editDistance(src[1:],dest) + 1
	edReplace = editDistance(src[1:],dest[1:]) + 1
	return min(min(edInsert,edDelete),edReplace)


class TagMemoRecord:
	def __init__(self,distance,refCount):
		self.distance = distance
		self.refCount = refCount

# 采用动态规划思想进行剪枝
# 引入状态的概念(i,j)
# 引入备忘录的概念
def editDistance2(src,dest,i,j,memo):
	print "second"
	if memo[i][j].refCount != 0:
		memo[i][j].refCount += 1
		return memo[i][j].distance
	distance = 0
	subi = len(src) - 1 - i 
	subj = len(dest) - 1 - j	

	if subi == 0:
		distance = subj
	elif subj == 0:
		distance = subi
	else:
		if src[i] == dest[j]:
			distance = editDistance2(src,dest,i+1,j+1,memo)
		else:
			edInsert = editDistance2(src,dest,i,j+1,memo) + 1
			edDelete = editDistance2(src,dest,i+1,j,memo) + 1
			edReplace = editDistance2(src,dest,i+1,j+1,memo) + 1
			distance = min(min(edInsert,edDelete),edReplace)
	memo[i][j].distance = distance
	memo[i][j].refCount = 1
	return distance

# 递推关系
# d[i,j] = d[i,j] + 0      source[i] == target[j]
# d[i,j] = min(d[i,j-1]+1,d[i-1,j]+1,d[i-1,j-1]+1)  source[i] != target[j]
# 边界条件：
# if len(target) == 0:
# 	d[i,0] = len(source)
# if len(source) == 0:
# 	d[0,j] = len(target)
# 直接利用状态递推关系实现动态规划算法（非递归）

def editDistance3(src,dest):
	d = [ [ 0 for j in range(len(dest)+1) ] for i in range(len(src)+1) ]
	for i in range(len(src)+1):
		d[i][0] = i
	for j in range(len(dest)+1):
		d[0][j] = j
	print d
	for i in range(1,len(src)+1):
		for j in range(len(dest)+1):
			print "thrid"
			if src[i-1] == dest[j-1]:
				d[i][j] = d[i-1][j-1]
			else:
				edInsert = d[i][j-1] + 1
				edDelete = d[i-1][j] + 1
				edReplace = d[i-1][j-1] +1
				d[i][j] =  min(min(edInsert,edDelete),edReplace)
	print d
	return d[len(src)][len(dest)]
	
	
print '-'*50,"editDistance"
src = ["s","n","o","w","y"]
dest = ["s","u","n","n","y"]
print editDistance(src,dest)


print '-'*50,"editDistance2"
src = ["s","n","o","w","y"]
dest = ["s","u","n","n","y"]
memo = [ [ TagMemoRecord(0,0) for j in range(len(dest)) ] for i in range(len(src)) ]
print editDistance2(src,dest,0,0,memo)

print '-'*50,"editDistance3"
src = ["s","n","o","w","y"]
dest = ["s","u","n","n","y"]
print editDistance3(src,dest)

