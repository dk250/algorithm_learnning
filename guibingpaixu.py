# 归并排序算法
# 归并排序算法时间复杂度为O(nlogn)
# 空间复杂度为O(n)，合并的时候，需要额外去申请空间。所以没有快速排序那么经常被人使用到
# 它是一个稳定的排序算法

data = [3, 2, 1]

def merge(data, first_array, second_array, begin_index, end_index):
	temp = []

	count = len(first_array)
	if count < len(second_array):
		count = len(second_array)

	i = 0
	j = 0

	for index in range(0,count):
		if i >= len(first_array) or j >= len(second_array):
			break

		if first_array[i] >= second_array[j]:
			temp.append(first_array[i])
			del first_array[i]
			i = i + 1
		else:
			temp.append(second_array[j])
			j = j + 1
			del second_array[j]
			
	if len(first_array) != 0:
		for value in first_array:
			temp.append(value)
	else:
		for value in second_array:
			temp.append(value)

	tempIndex = 0
	for index in range(begin_index,end_index + 1):
		data[index] = temp[tempIndex]
		tempIndex = tempIndex + 1
		

def sub_pai_xu(data, start, end):
	if start >= end:
		return

	middle = int((start + end) / 2)
	print(middle)

	sub_pai_xu(data, start, middle)
	result_array = data[start : middle]
	sub_pai_xu(data, middle+1, end)
	result_array2 = data[middle + 1 :]
	merge(data, result_array, result_array2, start, end)


def paixu(data):
	sub_pai_xu(data, 0, len(data) - 1)


paixu(data)

print(data)


