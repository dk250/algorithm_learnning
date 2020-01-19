#选择排序算法
#这是非稳定的算法，因为排序前后，相同元素的位置可能发生变化

data = [6, 5, 4, 3, 2, 1]

def xuanze(data):
	for index in range(0,len(data)):
		position_index = index
		min_value = data[index]
		should_change_position = 0
		for index2 in range(index,len(data) - 1):
			if min_value > data[index2 + 1]:
			 	min_value = data[index2 + 1]
			 	position_index = index2 + 1
			 	should_change_position = 1

		if should_change_position == 1:
			temp_value = data[index]
			data[index] = min_value
			data[position_index] = temp_value
		
xuanze(data)

print(data)

