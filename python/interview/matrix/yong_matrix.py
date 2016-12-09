#coding:utf-8

# 杨氏矩阵
# 每一行每一列都严格单调递增
# 如果将a[k]中的数填完后，矩阵中仍有空间，则填入 ∞

def getOrder(matrix,k):
	m = len(matrix)
	n = len(matrix[0])
#	print 'm',m,'n',n
	row = 0
	col = n - 1
	order = 0
	while row <= m - 1 and col >= 0:
#		print matrix[row][col],row,col,order
		if matrix[row][col] < k:
			order += col + 1
			row += 1
		else:
			col -= 1
	return order

matrix=[[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]]
print 'getOrder',getOrder(matrix,3)

print '-------------------'

def find_kth(matrix,k):
	m = len(matrix)
	n = len(matrix[0])	
	if m > k:
		m = k
	if n > k:
		n = k
	low = matrix[0][0]
	high = matrix[m-1][n-1]
	mid = 0

	# 二分法查找
	while low <= high:
		mid = (low + high) >> 1
		order = getOrder(matrix,mid)
		if order == k:
			break
		if order > k:
			high = mid - 1
		else:
			low = mid + 1
	row = 0
	col = n - 1
	ret = 0
	# 找出比mid 小的最大数
	while row <= m - 1 and col >= 0:
		print 'matrix',matrix[row][col]
		if matrix[row][col] < mid:
			if matrix[row][col] > ret:
				ret = matrix[row][col]
			row += 1
		else:
			col -= 1
	return ret

matrix=[[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]]
print "find_kth",find_kth(matrix,12)
