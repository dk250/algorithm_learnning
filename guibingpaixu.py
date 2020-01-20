# 归并排序算法

data = [6, 5, 4, 3, 2, 1]

def merge(first_array, second_array):
	temp = []

	count = len(first_array)

	if count < len(second_array):
		count = len(second_array)

   	i = 0
   	j = 0

	for index in range(0,count):
		if first_array[i] >= second_array[j]:
			temp.append(first_array[i])
			del first_array[i]
			i = i + 1
		else:
			temp.append(second_array[j])
			j = j + 1
			del second_array[j]

		if len(first_array) == 0 or len(second_array) == 0:
			break

	if len(first_array) != 0:
		temp.append(first_array)
	else:
		temp.append(second_array)



		

def sub_pai_xu(data, start, end):
	if start >= end:
		return

	middle = (start + end) / 2

	sub_pai_xu(data, start, middle)
	sub_pai_xu(data, middle + 1, start)


def paixu(data):
