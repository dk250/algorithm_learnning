# 插入排序算法实现


data = [6, 5, 4, 3, 2, 1]

def insert_sort(data):
	for index in range(0,len(data) - 1):
		if data[index] > data[index + 1]:
		 	for index2 in range(0,index + 1):
		 		if data[index + 1 - index2] < data[index - index2]:
		 			temp = data[index + 1 - index2]
		 			data[index + 1 - index2] = data[index - index2]
		 			data[index - index2] = temp



insert_sort[data]

print(data)


