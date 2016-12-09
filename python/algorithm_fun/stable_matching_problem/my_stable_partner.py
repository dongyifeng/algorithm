#coding:utf-8

# 稳定舞伴匹配问题：有n个男孩和n个女孩参加舞会，每个男孩和女孩均交给主持人一个名单，写上他(她)中意的舞伴的名字，排在前边的是最中意的舞伴。试问主持人在收到名单后，怎么分配使每个人都能和他们中意的舞伴结伴跳舞，避免舞会上出现不和谐的情况？

class TagPartner:
	def __init__(self,name,current,count,perfect):
		self.name = name
		self.current = current
		self.count = count
		self.perfect = perfect
	def isSingle(self):
		return self.current == None
	def position(self,name):
		return self.perfect.index(name)

man = [TagPartner("li_lei",None,0,["han_meimei","lu_se","rose","abby" ]),TagPartner("yang_peng",None,0,["han_meimei","rose","lu_se","abby"]),TagPartner("liang_yuancheng",None,0,["abby","han_meimei","lu_se","rose"]),TagPartner("dong_zehao",None,0,[ "rose","lu_se","han_meimei","abby" ])]

woman = {"abby":TagPartner("abby",None,0,["li_lei","dong_zehao","liang_yuancheng","yang_peng"]),"rose":TagPartner("rose",None,0,["li_lei","yang_peng","liang_yuancheng","dong_zehao"]),"han_meimei":TagPartner("han_meimei",None,0,["li_lei","liang_yuancheng","dong_zehao","yang_peng"]),"lu_se":TagPartner("lu_se",None,0,["yang_peng","li_lei","dong_zehao","liang_yuancheng"])}

def isCompleted(array):
	for item in array:
		if item.current == None:
			return False
	return True
def printResult(array):
	print "macthed result:"
	for item in array:
		print (item.name,item.current.name)
def run():
	while not isCompleted(man):
		for m in man:
			if not m.isSingle():
				continue
			for name in m.perfect[m.count:-1]:
				w = woman[name]
				if w.isSingle():
					m.current = w
					w.current = m
					m.count += 1
					break
				else:
					p = w.position(w.current.name)
					m_p = w.position(m.name)
					if m_p < p:
						w.current.current = None
						m.current = w
						w.current = m
						m.count += 1
	printResult(man)

run()	
