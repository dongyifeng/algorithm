#coding:utf-8

# 三等分
# [2,2,7,1,1,1,1,9,2,1,1]
# 7 和 9 将数组分为三段，第一段和为4，第二段为4，第三段为4，那么我认为7，9 是数组的三等的点（注意分割点不参与求和）
# i1 和 i2 将数组分为三段，当s1 == s3 and s1 == s2 时，则i1，i2 是三等分点。
# 如果 s1 < s3 ，这向右移动i1，促使s1 与 s3 相等，反之移动i2，促使s3 与 s1 相等。 

def run(data):
	if data is None or len(data) < 5:return None
	n = len(data)
	i1 = 1
	i2 = n - 2
	s1 = sum(data[:i1])
	s2 = sum(data[i1+1:i2])
	s3 = sum(data[i2+1:])
	while i2 - i1 >= 2:
		if s1 == s2 and s1 == s3:
			return (i1,i2)
		if s1 < s3:
			s1 += data[i1]
			i1 += 1
			s2 -= data[i1]
		else:
			s3 += data[i2]
			i2 -= 1
			s2 -= data[i2]
	return None



data = [2,2,7,1,1,1,1,9,2,1,1]
print data
print run(data)

data = [2,1,2,7,1,1,1,1,9,2,1,1]
print data
print run(data)
