#coding:utf-8

# 完全平方数
# 性质1：末位数只能是0,1,4,5,6,9
# 性质2：奇数的平方的个位数字一定是奇数，偶数的平方的个位数一定是偶数。
# 性质3：如果十位数字是奇数，则它的个位数字一定是6；反之也成立
# 性质4：偶数的平方是4的倍数；奇数的平方是4的倍数加1
# 性质5：奇数的平方是8n+1型；偶数的平方为8n或8n+4型。
# 性质6：形式必为下列两种之一：3k,3k+1
# 性质7：不是5的因数或倍数的数的平方为5k+-1型，是5的因数或倍数的数为5k型。
# 性质8：形式具有下列形式之一：16m,16m+1,16m+4,16m+9
# 性质9：数字之和只能是0,1,4,7,9
# 性质10：为完全平方数的充分必要条件是b为完全平方数
# 性质11：如果质数p能整除a，但p的平方不能整除a，则a不是完全平方数。
# 性质12：在两个相邻的整数的平方数之间的所有整数都不是完全平方数。
# 性质13：一个正整数n是完全平方数的充分必要条件是n有奇数个因数（包括1和n本身）
import math

# 利用了性质1

def isPerfectSquare(n):
	t = math.sqrt(n)
	t_int = int(t)
	return t == t_int

def perfectSquare(n):
	g = {0,1,4,5,6,9}
	for i in range(n):
		j = i % 10
		if j not in g:
			continue
		t = math.sqrt(i)
		t_int = int(t)
		if t == t_int:	
			print i

perfectSquare(100)

print "--------------"

def run(n):
	result = {}
	t = n % 10
	result[t] = 1
	while True:
		n = int( n / 10 )
		if n == 0:return result
		t = n % 10
		if t in result:
			result[t] += 1
		else:
			result[t] = 1
	return result

def containsDoubleNum(n):
	array = run(n)
	for key in array:
		if( array[key] > 1 ):return True
	return False


def main(n):
	for i in range(n):
		if isPerfectSquare(i) and containsDoubleNum(i):
			print i
			

n = 138
print containsDoubleNum(n)
main(99999)
print containsDoubleNum(n)
print containsDoubleNum(144)
