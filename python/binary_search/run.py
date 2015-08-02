
def rank(key,data):
	start=0
	end=len(data)-1
	while(start<=end):
		middle=(start+end)/2
		print "start:"+str(start)+";end:"+str(end)+";middle:"+str(middle)
		if(data[middle]<key):start=middle+1
		elif(data[middle]>key):end=middle-1
		else:return middle
	return None 
	
key=9
data=[1,2,3,4,5,6,7,8,9]	
print(rank(key,data))
