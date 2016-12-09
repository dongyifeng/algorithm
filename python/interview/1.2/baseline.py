
def containString(a,b):
	if len(a) < len(b):return False
	for i in b:
		tmp = False
		for j in a:
			if i == j:
				tmp =True
				break
		if not tmp:
			return False
	return True

a=["A","B","C","E"]
b=["B","C","E"]
print containString(a,b)	
