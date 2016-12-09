#coding:utf-8

# 栈：先进后出
# stack = []
# stack.append(1)
# stack.append(2)
# stack.pop() 2
# stack.pop() 1

# 队列:先进先出
# queue = []
# queue.append(1)
# queue.append(2)
# queue.pop(0) 1
# queue.pop(0) 2

# 或者
# queue = []
# queue.insert(0,1)
# queue.insert(0,2)
# queue.pop() 1
# queue.pop() 2

# 元素出入栈顺序合法性判断
# 分析:在内部s模拟堆栈即可，如果当前要出栈的元素恰好在栈顶，则必须出栈，否则入栈。（注意：in 和 out 长度必须相等）


def run(inArray,outArray):
	if len(inArray) != len(outArray):return False
	s = []
	i = j = 0
	while j < len(outArray): 
		while len(s) == 0 or s[len(s)-1] != outArray[j]:
			if i >= len(inArray):return False
			s.append(inArray[i])
			i += 1
		s.pop()
		j += 1
	return True

inArray = [1,2,3,4,5]
outArray = [4,5,3,2,1]
print inArray
print outArray
print run(inArray,outArray)


inArray = [1,2,3,4,5]
outArray = [4,5,3,1,2]
print run(inArray,outArray)
