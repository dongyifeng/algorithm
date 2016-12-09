#coding:utf-8

# 查找最大子零阵

def run(m):
	row_count = len(m)
	col_count = len(m[0])
	result = 0
	for i in range(row_count):
		for j in range(col_count):
			if m[i][j] != 0:continue
			k = i
			h = j
			t = 0
			while k < row_count and h < col_count:
				t += 1	
				contains_one = False
				for y in range(t):
					if m[k+t][h+y] != 0:
						contains_one = True
						break
				if contains_one:
					result = max(t,result)
					break
				for y in range(t):
					if m[h+y][j+t] != 0:
						contains_one = True
						break
				if contains_one:
					result = max(t,result)
					break
			i = t + i
	return result

