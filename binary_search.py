A = [-5,-3,-2,0,3,5,7]

#naive O(n) searching algorithm
# if 7 in A:
#     print(True)

#Traditional Binary Search - Looking if a number is in a sorted array
def binary_search(arr, target):

    N = len(arr)
    L = 0
    R = N - 1 

    while L <= R:
        M = L + ((R - L) // 2)

        if arr[M] == target:
            return True
        elif target < arr[M]:
            R = M - 1
        else:
            L = M + 1
        
    return False

binary_search(A,7)