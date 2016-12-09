#coding:utf-8

# 事实上，当我们令currSum为当前最大子数组的和，maxSum为最后要返回的最大子数组的和，当我们往后扫描时，
#    对第j+1个元素有两种选择：要么放入前面找到的子数组，要么做为新子数组的第一个元素；
#        如果currSum加上当前元素a[j]后不小于a[j]，则令currSum加上a[j]，否则currSum重新赋值，置为下一个元素，即currSum = a[j]。
#    同时，当currSum > maxSum，则更新maxSum = currSum，否则保持原值，不更新

def run(data):
	if data is None or len(data) == 0: return
	currentSum = 0
	maxSum = data[0]
	for i in data:
		if i + currentSum > i:
			currentSum +=i
		else:
			currentSum = i
		maxSum = max(currentSum,maxSum)
	return maxSum

data = [1,-2,3,10,-4,7,2,-5]
print run(data)
