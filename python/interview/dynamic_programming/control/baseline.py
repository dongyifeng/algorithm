#coding:utf-8

# 递归

def run(a1,a2,t1,t2,i,path):
	if i == 1:
		f1 = a1[i] + t2[i-1]
		f2 = a2[i] + t1[i-1]
		if f1 < f2:
			path.append(a1[i])
		else:
			path.append(a2[i])
		return (f1,f2)
	(f1,f2) = run(a1,a2,t1,t2,i-1,path)
	l1 = f1 + a1[i]
	l2 = f2 + a1[i] + t2[i-1]
	
	l3 = f2 + a2[i] 
	l4 = f1 + a2[i] + t1[i-1]
	f1 = min(l1,l2)
	f2 = min(l3,l4)
	if f1 < f2:
		path.append(a1[i])
	else:
		path.append(a2[i])

	return (f1,f2)

def run_for(a1,a2,t1,t2,path):
	f1 = a1[1] + t2[0]
	f2 = a2[1] + t1[0]
	if f1 < f2:
		path.append(a1[1])
	else:
		path.append(a2[1])
	for i in range(2,len(a1)):
		l1 = f1 + a1[i]
		l2 = f2 + a1[i] + t2[i-1]
		l3 = f2 + a2[i]
 	        l4 = f1 + a2[i] + t1[i-1]
	    	f1 = min(l1,l2)
 	        f2 = min(l3,l4)
		if f1 < f2:
			path.append(a1[i])
		else:
			path.append(a2[i])
	return (f1,f2)

a1 = [0,7,9,3,4,8,4]
t1 = [4,2,3,1,3,4,3]
a2 = [0,8,5,6,4,5,7]
t2 = [2,2,1,2,2,1,2]
path = []
print run(a1,a2,t1,t2,len(a1)-1,path)
print path

path=[]
print run_for(a1,a2,t1,t2,path)
print path
