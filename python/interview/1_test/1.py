#coding:utf-8	

def test_map(data):
	tmp = {}
	for i in data:
		tmp[i] = tmp.get(i,0) + 1
	for j in tmp:
		if tmp[j] == 1:
			print j

a = 'abcabcef'
test_map(a)		
