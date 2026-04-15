def find_peak(arr):
    """Находит индекс максимального элемента в битоническом массиве"""
    left = 0
    right = len(arr) - 1
    
    while left < right:
        mid = (left + right) // 2
        
        if arr[mid] < arr[mid + 1]:
            # Мы на подъеме → пик справа
            left = mid + 1
        else:
            # Мы на спуске или на пике → пик слева или это сам mid
            right = mid
    
    return left  # Индекс пика

# Пример
arr = [1, 2, 3, 4, 5, 4, 3, 2, 1]
peak_index = find_peak(arr)
print(f"Пик на индексе {peak_index}, значение {arr[peak_index]}")
# Вывод: Пик на индексе 4, значение 5