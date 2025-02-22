def my_function():
    print("hello from a function")


my_function()


def my_function(fname):
    print(fname + " yadav ")


my_function("sushil")
my_function("sujeet")
my_function("sumit")


def my_function(fname, lname):
    print(fname + " " + lname)


my_function("sushil", "yadav")


def my_function(*familymembers):
    print("youngest member " + familymembers[2])


my_function("sushil", "sujeet", "sumit", "khushboo")


def my_function(child1, child2, child3, child4):
    print("youngest member " + child3)


my_function(child1="sushil", child3="sujeet", child2="sumit", child4="khushboo")


def my_function(**kid):
    print(kid["lname"])


my_function(lname="sushil", fname="")


def my_function(country="Norway"):
    print("I am from " + country)


my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")
