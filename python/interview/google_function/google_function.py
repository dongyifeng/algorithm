#coding:utf-8

# Google 方程式
# WWWDOT - GOOGLE = DOTCOM
# 每个字符代表0~9之间的数字。不能以0开头。

# 解决方法：穷举

import math

class TagCharItem:
	def __init__(self,c,v,leading):
		self.c = c
		self.v = v
		self.leading = leading

class TagCharValue:
	def __init__(self,used,value):
		self.used = used
		self.value = value

def searchingResult(ci,cv,index,callback):
	max_char_count = 6
	max_number_count = len(cv)
	print index
	if index == max_char_count:
		callback(ci)
		return
	for i in range(max_number_count):
		if isValueValid(ci[index],cv[i]):
			cv[i].used = True
			ci[index].value = cv[i].value
			searchingResult(ci,cv,index+1,callback)
			cv[i].userd = False
def isValueValid(ci,cv):
	return not (cv.value == 0 and ci.leading)

def onCharListReady(ci):
	minuend = [ "W","W","W","D","O","T" ]
	subtrahend = [ "G","O","O","G","L","E" ]
	diff = [ "D","O","T","C","O","M" ]
	
	m = makeIntegerValue(ci,minuend)
	s = makeIntegerValue(ci,subtrahend)
	d = makeIntegerValue(ci,diff)
	print m,s,d
	if (m-s) == d:
		print m,"-",s,"=",d

def makeIntegerValue(ci,c):
	result = 0
	n = len(c)
	for i in range(n):
		for j in range(len(ci)):
			if ci[j].c == c[i]:
				result += ci[j].v * math.pow(10,n)
				n -= 1
	return result


ci = [TagCharItem("W",-1,True),TagCharItem("D",-1,True),TagCharItem("O",-1,False),TagCharItem("T",-1,False),TagCharItem("G",-1,True),TagCharItem("L",-1,False),TagCharItem("E",-1,False),TagCharItem("C",-1,False),TagCharItem("M",-1,False)]
cv = [TagCharValue(False,i) for i in range(11)]
index = 0
searchingResult(ci,cv,index,onCharListReady)

