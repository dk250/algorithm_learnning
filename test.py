
data = [2, 3, 1, 5, 7, 0]

def order(data, start, end):
	mark_value = data[start]
	low_array = []
	hight_array = []
	for value in data[start + 1 : end + 1]:
		if value <= mark_value:
			low_array.append(value)
		else:
			hight_array.append(value)

	for index in range(0, len(low_array)):
		data[start + index] = low_array[index]

	data[len(low_array)] = mark_value

	for index in range(0, len(hight_array)):
		data[len(low_array) + 1 + index] = hight_array[index]

	print(len(low_array))
	print(data)

	return len(low_array)
	
def kuaisupaixu(data, start, end):
	if start >= end:
		return
	
	middleIndex = order(data, start, end)
	# print(data)
	kuaisupaixu(data, start, middleIndex - 1)
	kuaisupaixu(data, middleIndex + 1, end)

def paixu(data):
	kuaisupaixu(data, 0, len(data))


paixu(data)
print(data)


# test = [1, 2, 3]

# for index in test[1:2]:
# 	print(index)

