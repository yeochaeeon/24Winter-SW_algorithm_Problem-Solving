def linear_search(arr, target):
    # print("linear search")
    for i, value in enumerate(arr):
        if value == target:
            return i 
    return -1

def binary_search(arr,target):
    # print("binary search")
    left, right = 0, len(arr)-1
    while left <= right : 
        mid = (left + right) // 2
        if arr[mid] == target: 
            return mid
        elif arr[mid] < target : 
            left = mid + 1 
        else : #arr[mid] >  target:
            right = mid - 1
    return -1