#Quick-sort
#Time:O(nlogn)(average case, technically worst case O(n^2))
#Space:O(n)

E = [-1,-3,-5,-3,5,6,-4,-6,8,0]

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    p = arr[-1]

    L = [x for x in arr[:-1] if x <= p]
    R = [x for x in arr[:-1] if x > p]

    L = quick_sort(L)
    R = quick_sort(R)
    print(L + [p] + R)

    return L + [p] + R

print(quick_sort(E))
