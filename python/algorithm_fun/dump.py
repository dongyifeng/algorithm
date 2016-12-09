#coding:utf-8

# 三个水桶等分8升水的问题

import pdb

BUCKETS_COUNT = 3
BUCKET_CAPICITY = [8,5,3]
BUCKET_INIT_STATE = [8,0,0]
BUCKET_FINAL_STATE = [4,4,0]

class TagAction:
	def __init__(self,f,t,water):
		self.f = f
		self.t = t
		self.water = water

class BucketState:
	def __init__(self,buckets=None):
		if buckets is None:
			self.buckets = BUCKET_INIT_STATE
		else:
			self.buckets = buckets
		self.curAction = self.setAction(8,-1,0)

	def copyStateArray(self,f,t,c):
		for i in range(c):
			t[i] = f[i]

	def setAction(self,w,f,t):
		action = TagAction(f,t,w)	
		self.curAction = action

	def isBucketEmpty(self,bucket):
		assert ( bucket >= 0 and bucket < BUCKETS_COUNT )
		return self.buckets[bucket]==0
	
	def isBucketFull(self,bucket):
		assert (bucket >= 0 and bucket < BUCKETS_COUNT)
		return self.buckets[bucket] >= BUCKET_CAPICITY[bucket]

	def isFinalState(self):
		return self.isSameBucketState(BucketState(BUCKET_FINAL_STATE))

	def canTakeDumpAction(self,f,t):
		if f < 0 or f >= BUCKETS_COUNT or t < 0 or t >= BUCKETS_COUNT:return False
		# 不是同一个桶，且from 桶中有水，且to 桶中不满
		if f != t and not self.isBucketEmpty(f) and not self.isBucketFull(t):
			return True
		return False
	
	def getBuckets(self,bucketWater):
		self.copyStateArray(bucketWater,self.buckets,BUCKETS_COUNT)

	def setBuckets(self,bucketWater):
		print 'bucketWater',bucketWater,'self.buckets',self.buckets
		self.copyStateArray(bucketWater,self.buckets,BUCKETS_COUNT)

	def dumpWater(self,f,t):
		bucketWater = [i for i in self.buckets ]
		# 将要倒出的水（容器容量-已盛水量）
		dump = BUCKET_CAPICITY[t] - bucketWater[t]
		# f 中水流大于需要倒出的水量
		if bucketWater[f] >= dump:
			bucketWater[t] += dump
			bucketWater[f] -= dump
		# 将f 中所有的水导入t中
		else:
			bucketWater[t] +=  bucketWater[f]
			dump= bucketWater[f]
			bucketWater[f] = 0
		if dump > 0:
			n = BucketState(bucketWater)
			n.setAction(dump,f,t)
			return n
		return None	 

	# 判断两个状态是否相同
	def isSameBucketState(self,state):
		for i in range(BUCKETS_COUNT):
			if self.buckets[i] != state.buckets[i]:
				return False
		return True

	def printStates(self):
		if self.curAction is not None:
			print "Dump:",self.curAction.water,"water from",self.curAction.f,"to",self.curAction.t+1,";"
		print "buckets water states is:"
		for i in range(BUCKETS_COUNT):
			print self.buckets[i],
		print ""

def isProcessedState(states,newState):
	for item in states:
		if item.isSameBucketState(newState):
			return True
	return False

def printResult(states):
	print "Find Result:"
	for item in states:
		item.printStates()

def searchStateOnAction(states,current,f,t):
	if not current.canTakeDumpAction(f,t):return
	# 从 from 到 to 倒水，如果成功，返回倒水后的状态
	n = current.dumpWater(f,t)
	if n is not None and not isProcessedState(states,n):
		states.append(n)
		searchState(states)
		states.pop();

def searchState(states):
	current = states[-1]
	if current.isFinalState():
		printResult(states)
		print '-'*50
		return
	# 使用双重循环排列组合各种倒水状态
	for j in range(BUCKETS_COUNT):
		for i in range(BUCKETS_COUNT):
			searchStateOnAction(states,current,j,i)



states = []
init = BucketState()
print init.buckets
states.append(init)
searchState(states)
print init.buckets
