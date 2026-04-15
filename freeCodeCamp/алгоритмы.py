def find_peak(arr):
    """Находит индекс пика (максимума) в битоническом массиве"""
    left, right = 0, len(arr) - 1
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < arr[mid + 1]:
            left = mid + 1
        else:
            right = mid
    return left

def binary_search_ascending(arr, left, right, target):
    """Бинарный поиск в ВОЗРАСТАЮЩЕМ массиве"""
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def binary_search_descending(arr, left, right, target):
    """Бинарный поиск в УБЫВАЮЩЕМ массиве"""
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:  # КЛЮЧЕВОЕ ОТЛИЧИЕ!
            left = mid + 1
        else:
            right = mid - 1
    return -1

def search_in_bitonic(arr, target):
    """Поиск любого элемента в битоническом массиве"""
    if not arr:
        return -1
    
    # Шаг 1: Находим пик
    peak_index = find_peak(arr)
    
    # Шаг 2: Ищем в левой (возрастающей) части
    result = binary_search_ascending(arr, 0, peak_index, target)
    if result != -1:
        return result
    
    # Шаг 3: Ищем в правой (убывающей) части
    result = binary_search_descending(arr, peak_index + 1, len(arr) - 1, target)
    return result