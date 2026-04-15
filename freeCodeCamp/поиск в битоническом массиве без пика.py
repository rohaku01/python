def search_in_bitonic_combined(arr, target):
    """Ищет элемент в битоническом массиве одним проходом"""
    left = 0
    right = len(arr) - 1
    
    # Сначала находим пик
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < arr[mid + 1]:
            left = mid + 1
        else:
            right = mid
    peak = left
    
    # Теперь ищем в нужной части
    if target == arr[peak]:
        return peak
    
    # Ищем в левой части
    left, right = 0, peak - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    # Ищем в правой части
    left, right = peak + 1, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1