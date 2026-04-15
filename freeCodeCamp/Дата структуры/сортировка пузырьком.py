def sort(arr):
    if len(arr) <= 1:
        return arr
    

    mid = len(arr) // 2
    
    left = sort(arr[:mid])
    right = sort(arr[mid:])
    sorted_list = []
    i = 0
    j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1
    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])
    return sorted_list

print(sort([2, 5, 6, 1, 7, 3]))



def bubble_optimized(arr):
    iterations = 0
    
    for i in range(len(arr)):
        swapped = False  # флаг, были ли замены
        for j in range(len(arr)-i-1):
            iterations += 1
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:  # если замен не было — выходим
            break
            
    return arr, iterations
        
print(bubble_optimized([5, 2, 8, 1, 9]))
        
    