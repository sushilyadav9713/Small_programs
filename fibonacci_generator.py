def fibonacci(limit):
    a,b = 0,1
    while a < limit:
        yield a
        a, b = b , a+b

fib = fibonacci(1000)
for i in fib:
    print(i)