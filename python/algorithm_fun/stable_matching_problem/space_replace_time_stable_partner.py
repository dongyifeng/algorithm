#coding:utf-8

# findFreeParner: 每次查找girl最喜欢boy时都需要遍历，实际情况下O(n^3),外层一边循环不能达到匹配完毕。
# 方案1：hash表。
# 方案2：用二维数组存储boys 和girls 个关系亲密的。

# 稳定舞伴匹配问题：有n个男孩和n个女孩参加舞会，每个男孩和女孩均交给主持人一个名单，写上他(她)中意的舞伴的名字，排在前边的是最中意的舞伴。试问主持人在收到名单后，怎么分配使每个人都能和他们中意的舞伴结伴跳舞，避免舞会上出现不和谐的情况？

import sys

class TagPartner:
	def __init__(self,name,current,nextIndex,perfect):
		self.name = name
		self.current = current
		self.nextIndex = nextIndex
		self.perfect = perfect
	def isSingle(self):
		return self.current == None
	def position(self,name):
		return self.perfect.index(name)

boys = [TagPartner("li_lei",None,0,[2]),TagPartner("yang_peng",None,0,[0,1,3,2]),TagPartner("liang_yuancheng",None,0,[0,2,3,1]),TagPartner("dong_zehao",None,0,[ 2,3,1,0 ])]

girls = [TagPartner("abby",None,0,[0,1]),TagPartner("rose",None,0,[0,1,2,3]),TagPartner("han_meimei",None,0,[3,2,0,1]),TagPartner("lu_se",None,0,[1,0,3,2])]

# 初始化girl 对boy 喜欢程度矩阵
def initPriority(boys,girls):
	priority = []
	for w in range(len(girls)):
		priority.append([sys.maxsize for i in range(len(boys))])
		pos = 0
		for m in girls[w].perfect:
			priority[w][m] = pos
			pos += 1

	return priority
def printResult(boys,girls):
	print "macthed result:"
	for item in boys:
		if item.current is None:
			print (item.name,"None")
			continue
		print (item.name,girls[item.current].name)

def findFreePartner(boys):
	for item in boys:
		# 如果男孩选完自己列表中女孩，但是还是单身,宁为玉碎，不为瓦全。
		if item.nextIndex >= len(item.perfect):continue
		if item.current is None:
			return boys.index(item)
	return -1

def galeShapley(boys,girls,pripority):
	boyId = findFreePartner(boys)
	while boyId >= 0:
		boy = boys[boyId]
		girlId = boy.perfect[boy.nextIndex]
		girl = girls[girlId]
		if girl.current is None:
			boy.current = girlId
			girl.current = boyId
		else:
			bpid = girl.current
			if pripority[girlId][boyId] < pripority[girlId][bpid]:
				boys[bpid].current = None
				boy.current = girlId
				girl.current = boyId
		boy.nextIndex += 1
		boyId = findFreePartner(boys) 
	printResult(boys,girls)

priority = initPriority(boys,girls)
print priority
galeShapley(boys,girls,priority)	
