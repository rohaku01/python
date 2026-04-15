def number_pattern(n):
    # Проверка типа
    if not isinstance(n, int):
        return 'Argument must be an integer value.'
    
    # Проверка значения
    if n < 1:
        return 'Argument must be an integer greater than 0.'
    
    # Создаем строку с числами от 1 до n через пробел
    result = ' '.join(str(i) for i in range(1, n + 1))
    return result

# Проверка
print(number_pattern(4))   # "1 2 3 4"
print(number_pattern(5))   # "1 2 3 4 5"
print(number_pattern(1))   # "1"