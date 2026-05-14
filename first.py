def fib(a):
    if a <= 1:
        return 0
    if a == 2:
        return 1
    return fib(a - 1) + fib(a-2)
    b,c = 0, 1
    for x in range(a):
        print(b)
        b,c = c,b+c
    return ""
print(fib(10))