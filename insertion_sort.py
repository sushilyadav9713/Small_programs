A = [-9,3,-5,-9,7,8,8,3,5,89]

def insertion_sort(arr):
    n = len(arr)
    for i in range(1,n):
        for j in range(i,0,-1):
            if arr[j-1]>arr[j]:
                arr[j-1],arr[j] = arr[j],arr[j-1]
            else:
                break

insertion_sort(A)
print(A)
