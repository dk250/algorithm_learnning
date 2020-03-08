# 快排是一种原地、不稳定的排序算法
# 原地排序算法
# 时间复杂度大部分情况下为O(nlogn)

data = [2, 1]

# 排序用到了两个数组，low_array数组存储小于或等于mark_value的数，high_array存储大于mark_value的数。
# 重点是重新赋值给原先数组的计算，要注意下标的值。
# python的切片真的有点骚,array[1:2] -> array[1], 可以理解成右边是开区间，两个参数是索引

def orderVersion1(data, start, end):
	mark_value = data[start]
	low_array = []
	high_array = []

	# 按照选取的mark_value，分类出比它大，以及比它小的两个数组
	for value in data[start + 1 : end + 1]:
		if value <= mark_value:
			low_array.append(value)
		else:
			high_array.append(value)

	# 如果有比mark_value小或者相等的数字，则要修改下数据data的元素顺序
	if len(low_array) > 0:
		for index in range(0, len(low_array)):
			data[start + index] = low_array[index]

		data[len(low_array) + start] = mark_value

		for index in range(0, len(high_array)):
			data[len(low_array) + 1 + index] = high_array[index]

	return len(low_array) + start


# 区别于orderVersion1的地方在于空间复杂度，orderVersion2是原地排序算法
def orderVersion2(data, start, end):
	finnal_index = start      # finnal_index用于记录下标志数的最终位置
	mark_value = data[start]

	for index in range(start+1, end):
		if data[index] <= mark_value:
			finnal_index += 1
			# 如果finnal_index 和 index 不相等，则说明遍历过的数组存在比mark_value大的数，需要替换下
			if finnal_index != index:
				temp_value = data[index]
				data[index] = data[finnal_index]
				data[finnal_index] = temp_value

	temp_value = data[finnal_index]
	data[start] = temp_value
	data[finnal_index] = mark_value

	return finnal_index



	
	
def kuaisupaixu(data, start, end):
	if start >= end:
		return
	
	middleIndex = orderVersion2(data, start, end)
	kuaisupaixu(data, start, middleIndex - 1)
	kuaisupaixu(data, middleIndex + 1, end)

def paixu(data):
	kuaisupaixu(data, 0, len(data))


paixu(data)
print(data)

