#coding:utf-8

# 解法一用的递归的方法有许多重复计算的工作，事实上，我们可以从后往前推，一步步利用之前计算的结果递推。
# 初始化时，dp[0]=dp[1]=1，然后递推计算即可：dp[n] = dp[n-1] + dp[n-2]

def run(k):
	if k <= 2:return k
	dp = [1,1,0]
	result = 0
	for i in range(2,k+1):
		dp[2] = dp[0] + dp[1]
		dp[0] = dp[1]
		dp[1] = dp[2]
		print dp[2]
	return dp[2]

k = 8
print run(k)
