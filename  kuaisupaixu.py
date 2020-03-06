
data = [2, 3, 1, 5, 7, 0, 7]

def order(data, start, end):
	mark_value = data[start]
	low_array = []
	hight_array = []
	for value in data[start + 1 : end + 1]:
		if value <= mark_value:
			low_array.append(value)
		else:
			hight_array.append(value)

	if len(low_array) > 0:
		for index in range(0, len(low_array)):
			data[start + index] = low_array[index]

		data[len(low_array) + start] = mark_value

		for index in range(0, len(hight_array)):
			data[len(low_array) + 1 + index] = hight_array[index]

	return len(low_array) + start
	
	
def kuaisupaixu(data, start, end):
	if start >= end:
		return
	
	middleIndex = order(data, start, end)
	kuaisupaixu(data, start, middleIndex - 1)
	kuaisupaixu(data, middleIndex + 1, end)

def paixu(data):
	kuaisupaixu(data, 0, len(data))


paixu(data)
print(data)


# test = [1, 2, 3]

# for index in test[1:3]:
# 	print(index)

