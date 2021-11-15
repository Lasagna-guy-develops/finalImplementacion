def fib(num):
    a, b = 1, 1
    list=[a,b]
    for _ in range(num - 1):
        a, b = b, a + b
        list.append(b)
    if num==1:
        return [1]
    else:
        return list