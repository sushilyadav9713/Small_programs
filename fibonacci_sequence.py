#Time: O(2^n)
#space:O(n)
def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    return fib(n-1) + fib(n-2)

print(fib(35))

#using memoization
#Time: O(N)
#Space: O(n)

def fib_memo(n):
    memo = {0:1,1:1}

    def f(x):
        if x in memo:
            return memo[x]
        else:
            memo[x] = f(x-1) + f(x-2)
            return memo[x]
        
    return f(n)

print(fib_memo(100))