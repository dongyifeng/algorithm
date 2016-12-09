
def containString(a,b):
	prime_number=[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59,61, 67, 71, 73, 79, 83, 89, 97, 101]
	a_ascii = ord("A")
	f = 1
	for i in a:
		x = prime_number[ord(i) - a_ascii]
		if ( f % x ) > 0 :
			f *= x
	for j in b:
		x = prime_number[ ord(j) - a_ascii ]
		if ( f % x ) > 0:
			return False
	return True

a=["A","B","C","E"]
b=["B","C","D"]
print containString(a,b)	
