#coding:utf-8

# 稳定婚姻匹配问题
# 稳定的意义：组合1：男A，女B；组合2：男C，女D。如果男A相对女B更喜欢女D，而女D相对于男C更喜欢男A，那么没有力量阻止男A与女D私奔，即不稳定。
# 数据：男对女的喜欢矩阵
#m1[w1,w2...wn]
#m2[w3,w2..w4]
#...
#mn[w11,w10..w1]

# 女对男的喜欢的矩阵
#w1[m1,m2...mn]
#w2[m3,m2..m4]
#...
#wn[m11,m10..m1]

# match[,,,,] 男孩i 匹配的女孩

# 贪心思路：所有男孩同时向各自最喜欢的女孩表白。
#	如果女孩a 只有1个女孩表白，接受男孩。
#	如果女孩a 有多个男孩表白，选择她最喜欢的男孩。
#	如果女孩没有男孩表白，静静等待下一轮

# 第K轮：所有单身男孩向各自第k喜欢的女孩表白。
#	如果女孩收到男孩的表白，如果女孩没有男友，接受，如果女孩现任男友j，女孩更喜欢男孩i，则女孩接受男孩i

def galeShapley(man,woman,macth):
	n = len(man)
	# wm[i][j]: 女孩i 对男孩j 的排名
	wm = [ [-1 for i in range(n)] for i in range(n) ]
	# choose[i]: 女孩i当前的男朋友 
	choose = [-1 for i in range(n)]
	# manIndex[i]: 男孩i被多少个女孩拒绝过
	manIndex = [-1 for i in range(n)]
	for i in range(n):
		for j in range(n):
			wm[i][woman[i][j]] = j
	single = False
	# 是否所有男孩都有了女朋友
	while not single:
		# 未发现单身男孩
		single = True
		# 每个男孩i 选择尚未被拒绝过的最喜欢的女孩
		for i in range(n):
			# 男孩i 已有女朋友
			if match[i] != -1:
				continue
			single = False
			manIndex[i] += 1
			j = manIndex[i]
			# 男孩i第j喜欢的女孩
			w = man[i][j]
			# 女孩w当前的男友
			m = choose[w]
			# 女孩没有男友，或者女孩更喜欢男孩i
			if m == -1 or wm[w][i] < wm[w][m]:
				match[i] = w
				choose[w] = i
				if m != -1:
					match[m] = -1
n = 4
man=[[2,3,1,0],
[2,1,3,0],
[0,2,3,1],
[1,3,2,0]]

woman=[[0,3,2,1],
[0,1,2,3],
[0,2,3,1],
[1,0,3,2]]

match = [-1 for i in range(n)]

galeShapley(man,woman,match)
print match
