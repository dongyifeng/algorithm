#coding:utf-8

def run(a1,a2):
	n = len(a1)
	m = len(a2[0])
	t = len(a1[0])
	r = [[ 0 for j in range(m) ]for i in range(n)]
	
	for i in range(n):
		for j in range(m):
			for k in range(t):
				r[i][j] += a1[i][k] * a2[k][j]

	return r


a1 = [[1,2],[3,4]]
a2 = [[0,1],[0,0]]
r = run(a1,a2)
print r
a1 = [[0,1],[0,0]]
a2 = [[1,2],[3,4]]
r = run(a1,a2)
print r
