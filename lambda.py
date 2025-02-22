x = lambda a: a + 7
print(x(4))

x = lambda a, b: a * b
print(x(5, 6))

x = lambda a, b, c: a + b + c
print(x(5, 6, 2))


def my_func(n):
    return lambda a: a * n


my_doubler = my_func(2)
print(my_doubler(11))
