n = int(input("Enter the number "))
def factorial(n):
    val = 1
    for i in range(1,n+1):
        val = val*i
    return val

print(factorial(n))