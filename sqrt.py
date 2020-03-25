a = 9
top = 9
end = 0
x = top / 2

while(abs(x ** 2 - a) > 0.000001):
    if x ** 2 > a:
        top = x
    elif x ** 2 < a:
        end = x
    else:
        break
    x = (top - end) / 2 + end

print(round(x, 6))
