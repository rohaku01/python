def search_in_descending(arr, target):
    """Ищет элемент в отсортированном по убыванию массиве"""
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:  # КЛЮЧЕВОЕ ОТЛИЧИЕ!
            # В убывающем массиве БОЛЬШИЕ элементы слева
            # Если текущий элемент БОЛЬШЕ target, значит target справа
            left = mid + 1
        else:  # arr[mid] < target
            # Если текущий элемент МЕНЬШЕ target, значит target слева
            right = mid - 1
    
    return -1

# Пример
arr = [13, 11, 9, 7, 5, 3, 1]
print(search_in_descending(arr, 7))   # 3
print(search_in_descending(arr, 10))  # -1