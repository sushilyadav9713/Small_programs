def f(n):
    if n == 1 or n ==0:
        return 1
    return n*f(n-1)

print(f(7))

#Part-2 -- find the number of trailing zeroes in that factorial
def trailing_zeroes(number):
    count = 0
    i = 5
    while(number//i != 0):
        count += int(number/i)
        i = i * 5
    return count
    
print(trailing_zeroes(10000))