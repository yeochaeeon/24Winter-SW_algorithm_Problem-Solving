# 1. 변수 -> RAM
# 2. 제어와 연산 -> CPU
# 1 + 2 == 함수 
# ----------------
# list, array의 특징
# 1. index가 존재하고 , index를 수정할 수 있다.
#   - but,index를 사용할 때는 에러에 주의 ( list index out of range )
# 2. 값 기반으로 변경 ( range based for 문 ..? )
#   - 속도가 개느림 
# def swap(a,b):
#     temp = a 
#     a = b
#     b = temp 
#     return (b,a)

def bubble_sort_v1(arr):
    n = len(arr)
    # for  _ in arr: # 속도 문제로 쓰지 않음  
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                # 구조 분해 할당 
                arr[j],arr[j+1] = arr[j+1],arr[j]
    return arr

def bubble_sort(arr):
    # print("bubble sort")
    ## bubble sort v2
    n = len(arr)
    # for  _ in arr: # 속도 문제로 쓰지 않음  
    for i in range(n-1):
        swapped = False
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                # 구조 분해 할당 
                arr[j],arr[j+1] = arr[j+1],arr[j]
                swapped = True
        if not swapped : 
            break
    return arr

## 재귀 함수 : 탈출 조건 부터 먼저 정한다 . 
def quick_sort(arr):
    # print("quick sort")
    #재귀 함수 
    # print(arr)
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2] 
    # list comprehensive
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot] 
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right) 

def merge_sort(arr):
    # print("merge sort")
    if len(arr) <=1:
        return arr

    mid = len(arr) // 2 
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left,right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    return result