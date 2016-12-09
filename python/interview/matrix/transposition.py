#coding:utf-8
# 矩阵倒置

# 将倒置矩阵 
def transposition(matrix):
	if matrix is None and len(matrix) > 0:return
	n = len(matrix)
	m = len(matrix[0])
	if m <= 0 :return
	r = [[0 for j in range(n)] for i in range(m)]	
	for i in range(n):
		for j in range(m):
			r[j][i] = matrix[i][j]
	return r


m = [[1,2,3],[4,5,6]]
print m
t = transposition(m)
print t
