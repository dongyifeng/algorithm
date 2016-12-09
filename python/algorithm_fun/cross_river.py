#coding:utf-8

# 有三个和尚和三个妖怪，在河的同一岸，要利用一条小船过河，小船每次只能载2个人，在两岸只要妖怪数量大于和尚数量，妖怪们就会吃掉和尚。需要安排一种过河方案，保证和尚和妖怪都能过河且和尚不能被妖怪吃掉。

MONK_COUNT = 3
MONSTER_COUNT = 3


class TagAction:
	def __init__(self,monk,monster,direction):
		self.monk = monk
		self.monster = monster
		self.direction = direction
class TagStates:
	def __init__(self,localMonk,localMonster,remoteMonk,remoteMonster,boat):
		self.localMonk = localMonk
		self.localMonster = localMonster
		self.remoteMonk = remoteMonk
		self.remoteMonster = remoteMonster
		self.boat = boat
		self.setAction(-1,-1,-1)

	def setAction(self,monk,monster,direction):
		newAction = TagAction(monk,monster,direction)	
		self.curAction = newAction

	def isFinalState(self):
		return self.localMonk == 0 and self.localMonster == 0 and self.remoteMonk == MONK_COUNT and self.remoteMonster == MONSTER_COUNT

	def canTakeTagAction(self,action):
		# 校验方向
		if self.curAction.direction == action.direction:
			return False
		# 数据正确性
		if self.localMonster + action.monster < 0 or self.localMonster + action.monster > MONSTER_COUNT:
			return False		
		if self.localMonk + action.monk < 0 or self.localMonk + action.monk > MONK_COUNT:
			return False
		return True

	# 校验和尚是否被吃，之所以跟canTakeTagAction 分开校验，isValidState 在coressRiver 之后调用，localMonk,localMonster,remoteMonk,remoteMonster 均更新过，直接比较就可以。如果在canTakeTagAction 需要将localMonk,localMonster,remoteMonk,remoteMonster 更新后值全部计算出来。
	def isValidState(self):
		if self.localMonk > 0 and self.localMonk < self.localMonster:
			return False
		if self.remoteMonk > 0 and self.remoteMonk < self.remoteMonster:
			return False
		return True

	def copy(self):
		return TagStates(self.localMonk,self.localMonster,self.remoteMonk,self.remoteMonster,self.boat)
	
	def coressRiver(self,action):
		nextNode = self.copy()
		nextNode.setAction(action.monk,action.monster,action.direction)
		nextNode.remoteMonk -= action.monk
		nextNode.remoteMonster -= action.monster
		nextNode.localMonk += action.monk
		nextNode.localMonster += action.monster
		nextNode.boat = action.direction
		return nextNode	 

	# 判断两个状态是否相同
	def isSameTagState(self,state):
		return self.curAction.direction == state.curAction.direction and self.remoteMonk == state.remoteMonk and self.remoteMonster == state.remoteMonster and self.localMonk == state.localMonk and self.localMonster == state.localMonster

	def printStates(self):
		if self.curAction is not None:
			print "cross_diver:monk_count:",self.curAction.monk,"monster",self.curAction.monster,"direction",self.curAction.direction,";"
		print "status:","localMonk",self.localMonk,"localMonster",self.localMonster,"remoteMonk",self.remoteMonk,"remoteMonster:",self.remoteMonster
		print ""

def isProcessedState(states,newState):
	for item in states:
		if item.isSameTagState(newState):
			return True
	return False

def printResult(states):
	print "Find Result:"
	for item in states:
		item.printStates()

def searchStateOnAction(states,current,action):
	if not current.canTakeTagAction(action):return
	n = current.coressRiver(action)
	
	if n.isValidState() and not isProcessedState(states,n):
		states.append(n)
		searchState(states)
		states.pop();

def searchState(states):
	current = states[-1]
	if current.isFinalState():
		printResult(states)
		print '-'*50
		return

	# 使用双重循环排列组合各种乘船的状态
	for action in ACTION:
		searchStateOnAction(states,current,action)

ACTION = [ TagAction(-1,0,1), TagAction(-2,0,1),TagAction(0,-1,1),TagAction(0,-2,1),TagAction(-1,-1,1),TagAction(1,0,0),TagAction(2,0,0),TagAction(0,1,0),TagAction(0,2,0),TagAction(1,1,0)]
init = TagStates(3,MONSTER_COUNT,0,0,0)
init.setAction(-1,-1,0)
#init = TagStates(0,1,3,2)
#print init.localMonk,init.localMonster,init.remoteMonk,init.remoteMonster
#print init.canTakeTagAction(2,0,0)

states = []
states.append(init)
searchState(states)
#init.canTakeTagAction(0,1,1)

#testData=[(0,2,1),(0,1,0),(0,2,1),(0,1,0),(2,0,1),(1,1,0),(2,0,1),(0,1,0),(0,2,1),(0,1,0),(0,2,1)]

#for item in testData:
#	init = init.coressRiver(item[0],item[1],item[2])
#init.printStates()
#print init.isFinalState()
