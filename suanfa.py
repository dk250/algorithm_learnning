data = [20, 10, 3, 11 , 1]

# 冒泡排序算法
# 1. 第二个循环不需要执行数组的长度
# 2. has_ever_change 如果没有需要再进行交换的数据，则说明已经排序完成了，可以停止循环
def maopao_sort(data):
	has_ever_change = 0
	for index in range(0, len(data)):
		value = data[0]
		for index2 in range(1,len(data) - index):
			nextValue = data[index2]
			if value > nextValue:
				data[index2 - 1] = nextValue
				data[index2] = value
				has_ever_change = 1
			else:
				value = nextValue
		if has_ever_change == 0:
			break

maopao_sort(data)

print(data)