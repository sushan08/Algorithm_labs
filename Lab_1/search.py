def linear_search(A, target):
    for i in range(len(A)):
        if A[i] == target:
            return i    
    return -1

def binary_search(A, target):
    left = 0
    right = len(A) - 1
    while left <= right:
        mid = (left + right) // 2
        if A[mid] == target:
            return mid
        elif A[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1