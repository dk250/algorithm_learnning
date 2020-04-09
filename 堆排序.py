class Heap:
    def __init__(self, max_count):
        self.max_count = max_count
        self.count = 0
        self.heap = [0]

    # 大顶堆的插入
    def insert_data_to_heap(self, data):
        if len(self.heap) > self.max_count:
            return
        self.count += 1
        self.heap.append(data)
        i = self.count

        while i > 0:
            if i // 2 > 0 and self.heap[i] > self.heap[i // 2]:
                temp = self.heap[i]
                self.heap[i] = self.heap[i // 2]
                self.heap[i // 2] = temp

                i = i // 2
            else:
                break

    # 自顶向下的堆化
    def heaify(self):
        index = 1
        while True:
            max_value = self.heap[index]
            max_index = index
            if index * 2 > self.count or index * 2 + 1 > self.count:
                break
            if max_value < self.heap[index * 2]:
                max_value = self.heap[index * 2]
                max_index = index * 2

            if max_value < self.heap[index * 2 + 1]:
                max_value = self.heap[index * 2 + 1]
                max_index = index * 2 + 1

            if max_index == index:
                break
            else:
                temp = self.heap[index]
                self.heap[index] = max_value
                self.heap[max_index] = temp
                index = max_index

    def remove_top_data(self):
        count = len(self.heap)
        self.heap[1] = self.heap[count -1]
        self.count -= 1
        self.heaify()


    def print_data(self):
        print(self.heap)



test_array = [5,6,7,8,1,2,9,16,13,15,22,27,21,33]
heap = Heap(20)
for value in test_array:
    heap.insert_data_to_heap(value)

heap.print_data()
heap.remove_top_data()
heap.print_data()

