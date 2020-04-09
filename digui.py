def find(n):
    if n == 1:
        return 1
    elif n== 2:
        return 2

    return find(n-1) + find(n-2)


resut = find(9)

print(resut)

# 如何改成for循环的写法, 其实这两个实现方式的想法有一些区别。
# 使用递归的想法是，f(n)的走法，可以分解为两个子问题，第一次走了一步的走法以及第一次走了两步的走法
# 循环的想法，走到第n步，只有两种可能，第一个是走了一步，第二个是走了两步。都是之前两种走法的和

def for_method(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2

    ret = 0
    pre = 2            # f(n-1)
    prepre = 1         # f(n-2)

    for index in range(3, n+1):
        ret = pre + prepre
        prepre = pre
        pre = ret

    return ret

result1 = for_method(9)
print(result1)