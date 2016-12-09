#coding:utf-8

# 字符串的替换和复制。
# 删除一个字符串所有的a，并且复制所有的b。注意：字符数组足够大。


def remove(charArray):
	n = 0
	numB = 0
	for i in range(len(charArray)):
		if charArray[i] != 'a':
			charArray[n] = charArray[i]
			n += 1
		if charArray[i] == 'b':
			numB += 1
	for i in range(n,len(charArray)):
		charArray[i] = "0"

# 类似插入排序O(n^2)
def copy1(charArray):
	n = len(charArray)
	i = 0
	while i < n:
		if charArray[i] == 'b':
			charArray.append("0")
			for j in range(len(charArray)-1,i,-1):	
				charArray[j] = charArray[j-1]
			charArray[i+1] = 'b' 
			i += 1
		i += 1

# “倒着”复制--惯用技巧O(n)
def copy2(charArray):
	numB = 0
	n = len(charArray)
	for i in range(n):
		if charArray[i] == 'b':
			charArray.append("0")
			numB += 1
	i = n - 1
	while i >= 0:
		charArray[i+numB] = charArray[i]
		if charArray[i] == 'b':
			numB -= 1
			charArray[i+numB] = charArray[i]
		i -= 1
	

charArray = ["s","b","a","m","b","c","a","e"]

print charArray
remove(charArray)
print charArray

print copy1(charArray)
print charArray
charArray = ["s","b","a","m","b","c","a","e"]
print "copy2",charArray
print copy2(charArray)
print charArray


# 思考题：如何将一个字符串中中空格变为%20(一种编码)
# 第一步：判断空格的个数
# 第二部：倒着复制
def run(charArray):
	numEmpty = 0
	n =len(charArray)
	for i in range(n):
		if charArray[i] == ' ':
			numEmpty += 1
			charArray.append("-1")
			charArray.append("-1")
	i = n - 1
	print charArray,numEmpty
	while i >=0:
		if charArray[i] == ' ':
			charArray[i+numEmpty*2] = "%"
			charArray[i+numEmpty*2-1] = "2"
			charArray[i+numEmpty*2-2] = "0"
			numEmpty -= 1
		else:
			charArray[i+numEmpty*2] = charArray[i]
		i -= 1


charArray = ["s"," ","a","m"," ","c","a","e"]
print 'run',charArray
run(charArray)
print charArray
