#coding:utf-8

# 一个字符串只包含*和数字，请把它的*号都放在开头


def swap(d,i,j):
	t = d[i]
	d[i] = d[j]
	d[j] = t

# 分析partition-- 数字相对顺序变化
def run(charArray):
	j = 0
	for i in range(len(charArray)):
		if charArray[i] == "*":
			swap(charArray,i,j)
			j += 1	
# 分析从后向前使用 partition-- 保证数据顺序
def run2(charArray):
	n = len(charArray)
	j = n - 1
	for i in range(j,-1,-1):
		if charArray[i].isdigit():
			swap(charArray,i,j)
			j -= 1	

# 通过倒复制--保证数字顺序不变
def run3(charArray):
	n = len(charArray)
	j = n - 1
	for i in range(j,-1,-1):
		if charArray[i].isdigit():
			charArray[j] = charArray[i]
			j -= 1
	for i in range(j+1):
		charArray[i] = '*'

charArray = ['*','0','1','*','2','*','4']
print charArray
run(charArray)
print charArray
charArray = ['*','0','1','*','2','*','4']
run2(charArray)
print charArray
charArray = ['*','0','1','*','2','*','4']
run3(charArray)
print charArray
