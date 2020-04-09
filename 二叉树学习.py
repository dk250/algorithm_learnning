import queue

class Node():
    def __init__(self,value,leftNode, rightNode):
        self.leftNode = leftNode
        self.rightNode = rightNode
        self.value = value


last_left_node = Node(1,None, None)
last_right_node = Node(2, None, None)

second_left_node = Node(3, last_left_node, last_right_node)
second_right_node = Node(4, None, None)

top_node = Node(10, second_left_node, second_right_node)


# 前序遍历的实现
def print_method(node):
    if node == None:
        return

    print(node.value)
    print_method(node.leftNode)
    print_method(node.rightNode)

# print_method(top_node)


# 层序遍历 TODO

# stack = []
#
# def ceng_print(node):
#     if node == None:
#         return
#     if len(stack) == 0:
#         print(node.value)
#         stack.append(node)
#         ceng_print(node)
#     else:
#         for index in range(0, len(stack)):


# 二叉查找
def find_node(node, value):
    if node == None:
        return False

    if node.value == value:
        return True
    elif node.value > value:
        return find_node(node.leftNode, value)
    else:
        return find_node(node.rightNode, value)

result = find_node(top_node, 1)

if result:
    print("find")