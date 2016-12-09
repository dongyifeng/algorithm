#coding:utf-8
# 未完成

def run(k):
	coin = [1,2,5,10]
	i = 0
	tmp = len(coin)/k
	arr = [1]
	while i < tmp:
		j = coin[i]
		while j < k:
			arr[j] += arr[j-coin[i]]
			j += 1
		i += 1
	return arr

k = 8
print run(k)
