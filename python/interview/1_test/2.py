#coding:utf-8

# 对称子字符串的最大长度
# 输入一个字符串，输出该字符串中对称的子字符串的最大长度。比如输入字符串“google”，由于该字符串里最长的对称子字符串是“goog”，因此输出4

def isPalindrome(data):
	i = 0
	j = len(data) - 1
	while i < j :
		if data[i] != data[j]:
			return False
		i += 1
		j -= 1
	return True

def calcMaxBalance(data):
	n = len(data)
	max_length = 0
	max_balance = ''
	for i in range(n):
		tmp1 = data[0:i-1]
		tmp2 = data[i:n]
		if isPalindrome(tmp1) and len(tmp1) > max_length:
			max_length = len(tmp1)
			max_balance = tmp1
		if isPalindrome(tmp2) and len(tmp2) > max_length:
			max_length = len(tmp2)
			max_balance = tmp2
	return (max_length,max_balance)
				

data = 'google'
print calcMaxBalance(data)


def partition(data):
	j = 0
	for i in range(len(data)):
		data.insert(j,'#')
		j += 2

def calcMaxBalance2(data):
	n = len(data)
	max_length =0
	for i in range(len(data)):
		if data[i] == '#':
			s = i - 1
			e = i + 1
			length = 0
			while s >=0 and e < n and data[e] == data[s]:
				s -= 1
				e += 1
				length +=1
			if length > max_length:
				max_length = length
	return max_length	


data = ['g','o','o','g','l','e']
partition(data)
print data
print calcMaxBalance2(data)
