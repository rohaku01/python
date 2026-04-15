def search_in_bitonic(arr, target):
    """Ищет элемент в битоническом массиве (сначала возрастает, потом убывает)"""
    
    # ШАГ 1: Находим пик
    left, right = 0, len(arr) - 1
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < arr[mid + 1]:
            left = mid + 1
        else:
            right = mid
    peak = left
    
    # ШАГ 2: Ищем в левой (возрастающей) части
    left, right = 0, peak
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    # ШАГ 3: Ищем в правой (убывающей) части
    left, right = peak + 1, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:  # Убывание!
            left = mid + 1
        else:
            right = mid - 1
    
    return -1  # Не найдено

# Пример
arr = [1, 3, 5, 7, 9, 8, 6, 4, 2]
print(f"Массив: {arr}")
print(f"Пик: {arr[4]} на индексе 4")
print(f"Ищем 5: {search_in_bitonic(arr, 5)}")   # 2
print(f"Ищем 6: {search_in_bitonic(arr, 6)}")   # 6
print(f"Ищем 9: {search_in_bitonic(arr, 9)}")   # 4
print(f"Ищем 10: {search_in_bitonic(arr, 10)}") # -1