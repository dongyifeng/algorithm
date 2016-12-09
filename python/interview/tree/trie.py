#coding:utf-8

# 字典树
# 字典树是一种树形结构，利用字符串的公共前缀来减少查询时间，以空间换时间；根节点不包含字符，除根节点外每一个节点都只包含一个字符；从根节点到某一节点，路径上经过的字符连接起来，为该节点对应的字符串。
# 如图是一个字典树，共有12个节点不为NULL，其中根节点不包含字符。那么这棵树中有几个单词呢？hell、hello、help、world，共四个单词。节点标记为红色表示根节点到该节点所形成的字符串存在。

class TrieNode:
	def __init__(self):
		self.flag = False
		MAX_CHAR = 26
		self.child = [None for i in range(MAX_CHAR)]
	# 递归插入一个单词，每次建立其中的一个字符
	def insert(self,word,i):
		pos = ord(word[i]) - ord('a')
		if self.child[pos] is None:
			self.child[pos] = new TrieNode
		# 若是最后一个字符，修改flag标记，否则递归插入
		if i == len(word) - 1:
			self.child[pos].flag = True
		else:
			self.insert(self,word,i+1)
		
	def search(self,word,i):
		pos = ord(word[i]) - ord('a')
		if self.child[pos] is None:return False
		# 若查找到了最后一个字符，当前节点的对应孩子的flag标记了该单词是否存在
		if i == len(word) - 1:
			return self.child[pos].flag
		# 否则递归校验
		return self.search(self,word,i+1)
		
	def startsWith(self,word,i):
		pos = ord(word[i]) - ord('a')
		if self.child[pos] is None:
			return False
		# 只要查找到最后一个字符前未失败说明以该单词为前缀的单词存在
		if i == len(word) - 1:
			return True
		return self.startsWith(self,word,i+1)
		

class Trie:
	def __init__():
		self.root = TrieNode()
	def insert(word):
		self.root.insert(word,0)
	def search(word):
		return self.root.search(word,0)
	def startsWith(word):
		return self.root.startsWith(word,0)
