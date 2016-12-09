#coding:utf-8

UNIT_COUNT = 5

class TagMaxMatch:
	def __init__(self):
		self.edge = [ [ None for j in range(UNIT_COUNT) ] for i in range(UNIT_COUNT) ]
		self.onPath = [ None for i in range(UNIT_COUNT) ]
		self.path = [ None for i in range(UNIT_COUNT) ]
		self.maxMatch = None


# 从xi 寻找增广路径
def findAugmentPath(match,xi):
	for yj in range(UNIT_COUNT):
		if match.edge[xi][yj] == 1 and not match.onPath[yj]:
			match.onPath[yj] = True
			if match.path[yj] == -1 or findAugmentPath(match,match.path[yj]):
				match.patch[yj] = xi
				return True
	return False
