#coding:utf-8

def calcFirstJoinPoint(data1,data2):
	i_1 = 0
	i_2 = 0
	tmp = {}
	for i in range(len(data1)):
		tmp[data1[i]] = i
	for i in range(len(data2)):
		if data2[i]  in tmp:
			i_2 = i
			i_1 = tmp[data2[i]]	
	return (i_1,i_2)

data1 = [11,15,2,13,14,16]
data2 = [1,2,3,4,5,6]

print calcFirstJoinPoint(data1,data2)
