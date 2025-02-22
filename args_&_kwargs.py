def foo(a,b,*args, **kwargs):
    print(a,b)
    for arg in args:
        print(arg)
    for key in kwargs:
        print(key,kwargs[key])

foo(1,2,3,4,six=6,eight=8)

def foo(a,b,c):
    print(a,b,c)

my_dict = {'a':1,'b':2,'c':3}
foo(**my_dict)