#bubble sort 
#Time: O(n^2)
#Space:O(1)

A = [-6,7,-4,5,3,0,-8,-9,-100]

def bubble_sort(arr):
    n = len(arr)
    flag = True
    while flag:
        flag = False
        for i in range(1,n):
            if arr[i-1]>arr[i]:
                arr[i],arr[i-1] =arr[i-1],arr[i]
                flag = True

bubble_sort(A)
print(A)