def binary_search(arr, target, start=None, end=None):
    
    start = 0 if start is None else start
    end = len(arr) - 1 if end is None else end
    
    while start <= end:
        mid = (start + end) // 2
    
        if arr[mid] < target:
            start = mid + 1
        elif arr[mid] > target:
            end = mid - 1
        else:
            return mid
    return []

print(binary_search([1,2,3,4,5,6,7], 5, 2, 5))
         
    
    
    
    
    
    