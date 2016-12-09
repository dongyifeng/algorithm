#coding:utf-8

numChar=["零","一","二","三","四","五","六","七","八","九"]
unitSection=["","万","亿","万亿"]
unitChar=["","十","百","千"]

import math

# 2000 亿 0101 万 0200 

def convert(num):
	sectionLength = 4
	l = getIntLen(num)
	w = int(math.ceil( l / float(sectionLength) ))
	result = ""
	for i in range(w):
		section = unitSection[i]
		tmpNum = getNum(num,sectionLength,i)
		notZore = False
		tmpResult = section
		print "tmpNum",tmpNum
		for j in range(sectionLength):
			unit = ""
			char = ""
			d = getNum(tmpNum,1,j)
			if d > 0:
				notZore = True
				unit = unitChar[j]
				char = numChar[d]
			if d == 0:
				# 规则1
				if not notZore:
					continue
				# 规则2
				if j == (sectionLength-1) and i < (w-1):
					char = numChar[d]
				# 规则3
				tmpD = tmpNum / int(math.pow(10,j))
				if tmpD > 0:
					char = numChar[d]
			tmpResult = char + unit + tmpResult
			print "tmpResult:",tmpResult
		result = tmpResult + result
	return result

def getNum(num,w,i):
	return int((num/math.pow( math.pow(10,w),i)) % math.pow(10,w))

def getIntLen(num):
	tmp = num
	count = 0
	while tmp > 0:
		count += 1
		tmp = tmp / 10
	return count
a = 200001010200
print a
r = convert(a)
print r


a = 10203
print convert(a)
