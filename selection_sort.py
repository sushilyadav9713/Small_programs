C = [-2,-3,-5,-6,-7,8,9,4,6,9,5,0]

#finds the minimum value in array in replace it with current value
#Time: O(n^2)
#Space: O(1)

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1,n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index],arr[i]

selection_sort(C)
print(C)
