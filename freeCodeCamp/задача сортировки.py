def selection_sort(arr):
    n = len(arr)
    
    comparisons = 0
    swaps = 0
    
    for i in range(n):
        min_index = i
        
        for j in range(i + 1, n):
            comparisons += 1
            if arr[j] < arr[min_index]:
                min_index = j
                
        if i != min_index:
            arr[i], arr[min_index] = arr[min_index], arr[i]
            swaps += 1
    return arr, comparisons, swaps
arr = [64, 25, 12, 22, 11]
sorted_arr, comp, swaps = selection_sort(arr.copy())

print(f"Отсортированный: {sorted_arr}")
print(f"Сравнений: {comp}")
print(f"Перестановок: {swaps}")










def quick_sort(arr):
    comparisons = 0
    swaps = 0
    if len[arr] <= 1:
        return arr, comparisons, swaps
    
    n = arr[0]
    left = []
    right = []
    
    for i in arr[1:]:
        comparisons += 1
        if i <= n:
            left.append(i)
            swaps += 1
        else:
            right.append(i)
            swaps += 1
    left_sorted, comp_left, swap_left = quick_sort(left)
    right_sorted, comp_right, swap_right = quick_sort(right)
    
    comparisons += comp_left + comp_right
    swaps += swap_left + swap_right
    
    return left_sorted + [n] + right_sorted, comparisons, swaps
    
        
    