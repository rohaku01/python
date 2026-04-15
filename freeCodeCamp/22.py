def square_root_bisection(square_target, tolerance=1e-7, max_iterations=100):
    """
    Вычисляет квадратный корень числа методом бинарного поиска.
    
    Args:
        square_target: Число, для которого вычисляется квадратный корень
        tolerance: Допустимая погрешность результата (по умолчанию 1e-7)
        max_iterations: Максимальное количество итераций (по умолчанию 100)
    
    Returns:
        Квадратный корень числа, или None если не удалось вычислить
    
    Raises:
        ValueError: Если число отрицательное
    """
    # Проверка на отрицательное число
    if square_target < 0:
        raise ValueError("Square root of negative number is not defined in real numbers")
    
    # Проверка на 0 и 1
    if square_target == 0 or square_target == 1:
        print(f"The square root of {square_target} is {square_target}")
        return square_target
    
    # Определяем границы поиска
    left = 0
    right = max(1, square_target)
    
    root = None
    
    # Бинарный поиск
    for i in range(max_iterations):
        mid = (left + right) / 2
        square = mid * mid
        
        # Проверяем достижение точности
        if abs(square - square_target) < tolerance: #if abs(mid * mid - square_target) < 2 * mid * tolerance: погрешность корня а не квадрата
            root = mid
            break
        elif square < square_target:
            left = mid
        else:
            right = mid
    
    # Проверяем результат
    if root is not None:
        print(f"The square root of {square_target} is approximately {root}")
        return root
    else:
        print(f"Failed to converge within {max_iterations} iterations")
        return None