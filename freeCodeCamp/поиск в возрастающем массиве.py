def search_in_ascending(arr, target):
    """Ищет элемент в отсортированном по возрастанию массиве"""
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1  # Ищем справа
        else:
            right = mid - 1  # Ищем слева
    
    return -1  # Не найдено

# Пример
arr = [1, 3, 5, 7, 9, 11, 13]
print(search_in_ascending(arr, 7))   # 3
print(search_in_ascending(arr, 10))  # -1