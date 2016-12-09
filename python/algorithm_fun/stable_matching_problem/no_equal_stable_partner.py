#coding:utf-8

# boys 和 girls 可以不相等
# 某个boy 特别讨厌某个girl ，打死也不和某个girl接合。

# 稳定舞伴匹配问题：有n个男孩和n个女孩参加舞会，每个男孩和女孩均交给主持人一个名单，写上他(她)中意的舞伴的名字，排在前边的是最中意的舞伴。试问主持人在收到名单后，怎么分配使每个人都能和他们中意的舞伴结伴跳舞，避免舞会上出现不和谐的情况？

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

li_lei = 0
yang_peng = 1
liang_yuancheng = 2
dong_zehao = 3

boys = [TagPartner("li_lei",None,0,[2]),TagPartner("yang_peng",None,0,[2,1,3,0]),TagPartner("liang_yuancheng",None,0,[0,2,3,1]),TagPartner("dong_zehao",None,0,[ 2,3,1,0 ])]

girls = [TagPartner("abby",None,0,[0,3,2,1]),TagPartner("rose",None,0,[0,1,2,3]),TagPartner("han_meimei",None,0,[3,2,0,1]),TagPartner("lu_se",None,0,[1,0,3,2])]

def printResult(boys,girls):
	print "macthed result:"
	for item in boys:
		if item.current is None:
			print(item.name,"None")
			continue
		print (item.name,girls[item.current].name)

def findFreePartner(boys):
	for item in boys:
		if item.nextIndex >= len(item.perfect):continue
		if item.current is None:
			return boys.index(item)
	return -1

def getPerfectPosition(girl,boyId):
	return girl.perfect.index(boyId)

def galeShapley(boys,girls):
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
			if getPerfectPosition(girl,boyId) < getPerfectPosition(girl,bpid):
				boys[bpid].current = None
				boy.current = girlId
				girl.current = boyId
		boy.nextIndex += 1
		boyId = findFreePartner(boys) 
	printResult(boys,girls)

galeShapley(boys,girls)	
