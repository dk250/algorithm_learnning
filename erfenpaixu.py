a = [1, 2, 3, 4, 5, 6]

# def find(a, target, begin, end):
#     if begin >= end:
#         if a[begin] == target:
#             return 1
#         else:
#             return 0
#
#     midlle_index = (end - begin) // 2 + begin
#     middle_value = a[midlle_index]
#     if target > middle_value:
#         find(a, target, midlle_index+1, end)
#     elif target < middle_value:
#         find(a, target, begin, midlle_index-1)
#     else:
#         return 1
#
# result = find(a, 4, 0, 5)
#
# if result:
#     print("find")
# else:
#     print("NotFind")

#也可以不用递归进行处理
#时间复杂度为O(logn)
#链表存储的数据，不适合使用二分查找法进行查找，因为链表随机访问的时间复杂度为O(n)，数组的随机访问时间复杂度为O(1)。数组需要连续的内存，所以导致太大的数据量，不适合使用二分查找法
#动态变化的数组集合，二分查找排序其实是不适合的


#使用循环的方式，进行二分查找

def findIndexWith(index, array):
    temp = array[index]
    result = index
    for i in range(index, len(array)):
        if temp != array[i]:
            result = i

    if result == index:
        result = len(array) - 1

    return result

def findVersion2(num, array):
    begin = 0
    end = len(array) - 1
    result = -1
    while(begin <= end):
        middle = (end - begin) // 2 + begin
        if num == array[middle]:
            result = middle
            return result
            break
        elif num > array[middle]:
            begin = middle + 1
        else:
            end = middle - 1

    return result

def findVersion3(num, array):
    begin = 0
    end = len(array) - 1
    result = -1
    while(begin <= end):
        middle = (end - begin) // 2 + begin

        if num > array[middle]:
            if array[middle - 1] < num:  #找出第一个小于指定数的值
                end = middle - 1
            # if array[middle + 1] < num: 找出最后一个小于指定数的值
            #     begin = middle + 1
            else:
                result = middle
                break
        else:
            end = middle - 1

    return result

def findVersion4(num, array):
    begin = 0
    end = len(array) - 1
    result = -1
    while(begin <= end):
        middle = (end - begin) // 2 + begin
        if num == array[middle]:
            if array[middle - 1] == num:
                end = middle -1
            else:
                result = middle
                break
        elif num > array[middle]:
            begin = middle + 1
        else:
            end = middle - 1

    return result

result = findVersion4(9, [1,1,9, 9 ,9, 10 ,11])

if result != -1:
    print("find" + str(result))
else:
    print("not find")