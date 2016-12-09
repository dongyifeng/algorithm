#coding:utf-8
# “最好的方法”，时间复杂度O(n + m)，空间复杂度O(1)
def containString(a,b):
	if len(a) < len(b):return False
	hash_int = 0
	a_ascii = ord("A")
	for i in a:
		hash_int |= (1 << (ord(i) - a_ascii ) )

	for j in b:
		if (hash_int & ( 1 << ord(j) - a_ascii )) == 0:
			return False
	return True

a=["A","B","C","E"]
b=["B","C","D"]
print containString(a,b)	
