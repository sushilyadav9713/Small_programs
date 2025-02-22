def my_function(food):
    for x in food:
        print(x)


fname = "sushil"
fruits = ["apple", "banana", "cherry"]
my_function(fruits)
my_function(fname)


def my_function(x):
    return 5 * x


print(my_function(3))
print(my_function(4))
print(my_function(5))


def my_function():
    pass


def my_function(x, /):
    print(x)


my_function(7)


def my_function(*, x):
    print(x)


my_function(x=7)


def my_function(a, b, /, *, c, d):
    print(a + b + c + d)


my_function(5, 6, c=7, d=8)
