#coding:utf-8

# 将一个0-1 串进行排序，你可以交换任意两个位置，问最少交换的次数。

# 分析：快排partition，最左边是的那些0和最右边的那些1都可以不管

def run(charArray):
	result = 0
	i = 0
	j = len(charArray) - 1
	while i < j:
		while i < j and charArray[i] == "0":
			i += 1
		while i < j and charArray[j] == "1":
			j -= 1
		if i < j:
			result += 1
		i += 1
		j -= 1
	return result

charArray = ["0","0","1","1","0","1","0","0","0","1"]
print run(charArray)
