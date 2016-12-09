#coding:utf-8

#定位法
#首先直接定位到最右上角的元素，再配以二分查找，比要找的数（6）大就往左走，比要找数（6）的小就往下走，直到找到要找的数字（6）为止，这个方法的时间复杂度O（m+n）。如下图所示：

def YangMatrix(m,v):
	if m is None:return
	row = 0
	col = len(m[0]) - 1
	while row < len(m) and col >= 0:
		print row,col
		if m[row][col] == v:
			return True
		if m[row][col] > v:
			col -= 1
		if m[row][col] < v:
			row += 1
	return False

m = [[1,2,8,9],[2,4,9,12],[4,7,19,13],[6,7,11,15]]
print YangMatrix(m,6)
print YangMatrix(m,5)
	
		
