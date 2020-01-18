# 插入排序算法实现


data = [6, 5, 3, 4, 2, 1]


# 第一个版本
# def insert_sort(data):
# 	for index in range(0,len(data) - 1):
# 		if data[index] > data[index + 1]:
# 		 	for index2 in range(0,index + 1):
# 		 		if data[index + 1 - index2] < data[index - index2]:
# 		 			temp = data[index + 1 - index2]
# 		 			data[index + 1 - index2] = data[index - index2]
# 		 			data[index - index2] = temp
# 		 		else:
# 		 			break

# 第二版本
def insert_sort(data):
	for index in range(0, len(data) - 1):
		if data[index] > data[index + 1]:
			value = data[index + 1]
			positionIndex = index + 1
			for j in range(index + 1, 0, -1):
				if value < data[j - 1]:
					data[j] = data[j-1]
					positionIndex = j - 1
				else:
					break
			data[positionIndex] = value


insert_sort(data)

print(data)


# 学习要点

# 1. 可以先不那么急的移动下一个排序的元素的位置
# 2. 因为是插入排序，说明之前的元素都已经排序好了，当循环到下一个元素没有比当前的元素大，则可以判定循环结束了。
# 2. range函数的使用，三个参数，第一个参数表示起点，第二个参数表示终点，左边是闭区间，右边是开区间，第三个参数代表步幅
