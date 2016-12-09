#coding:utf-8

# 01 背包问题
import sys

class TagObject:
	def __init__(self,weight,price,status):
		self.weight = weight
		self.price = price
		self.status = status # 0:未选中；1:已选中；2:已经不可选

# 根据优先选择价格最大的策略
def chooseMaxPrice(objs,c):
	index = -1
	maxPrice = 0
	for i in range(len(objs)):
		if objs[i].status == 0 and objs[i].price > maxPrice:
			maxPrice = objs[i].price
			index = i
	return index

def chooseMinWeight(objs,c):
	index = -1
	minWeight = sys.maxint
	for i in range(len(objs)):
		if objs[i].status == 0 and objs[i].weight < minWeight:
			minWeight = objs[i].weight 
			index = i
	return index

def chooseMaxDensity(objs,c):
	index = -1
	maxDensity = 0
	for i in range(len(objs)):
		density = (objs[i].price*1.0) / objs[i].weight
		if objs[i].status == 0 and density > maxDensity:
			maxDensity = density
			index = i
	return index


class TagKnapsackProblem:
	def __init__(self,objs,totalC):
		self.objs = objs
		self.totalC = totalC

def printResult(objs):
	sumPrice = 0
	sumWeight = 0
	for i in range(len(objs)):
		item = objs[i]
		if item.status == 1:
			sumPrice += item.price
			sumWeight += item.weight
			print i+1,item.weight,item.price

	print "sumPrice:",sumPrice,"sumWeight:",sumWeight
def greedyAlgo(problem,spFunc):
	ntc = 0
	# 每次选最符合策略的那个物品，最后再检查
	idx = spFunc( problem.objs,problem.totalC - ntc )
	while (idx != -1):
		item = problem.objs[idx]
		if ntc + item.weight <= problem.totalC:
			item.status = 1
			ntc += item.weight
		else:
			item.status = 2
		idx = spFunc( problem.objs,problem.totalC - ntc )


	printResult(problem.objs)

wi = [35,30,60,50,40,10,25]
pi = [10,40,30,50,35,40,30]
problem = TagKnapsackProblem([ TagObject(wi[i],pi[i],0) for i in range(len(wi)) ],150)

print '-'*50,"chooseMaxPrice"
greedyAlgo(problem,chooseMaxPrice)
print '-'*50,"chooseMinWeight"

problem = TagKnapsackProblem([ TagObject(wi[i],pi[i],0) for i in range(len(wi)) ],150)
greedyAlgo(problem,chooseMinWeight)
print '-'*50,"chooseMaxDensity"
problem = TagKnapsackProblem([ TagObject(wi[i],pi[i],0) for i in range(len(wi)) ],150)
greedyAlgo(problem,chooseMaxDensity)
