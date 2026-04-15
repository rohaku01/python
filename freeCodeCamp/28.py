def verify_card_number(card_number):
    """
    Проверяет номер карты по алгоритму Луна
    
    Аргументы:
        card_number: строка с номером карты (может содержать пробелы и дефисы)
    
    Возвращает:
        "VALID!" если номер действителен, "INVALID!" если нет
    """
    # Удаляем все дефисы и пробелы
    card_number = card_number.replace('-', '').replace(' ', '')
    
    # Проверяем, что все символы - цифры
    if not card_number.isdigit():
        return "INVALID!"
    
    # Переворачиваем строку для удобства обработки справа налево
    reversed_card = card_number[::-1]
    
    total = 0
    
    # Проходим по каждой цифре
    for i, char in enumerate(reversed_card):
        digit = int(char)
        
        # Если индекс НЕЧЕТНЫЙ (считая с 0) — удваиваем
        # Это соответствует каждой второй цифре, начиная справа
        if i % 2 == 1:
            digit *= 2
            # Если результат больше 9, складываем цифры (или вычитаем 9)
            if digit > 9:
                digit -= 9
        
        total += digit
    
    # Если сумма делится на 10, номер действителен
    if total % 10 == 0:
        return "VALID!"
    else:
        return "INVALID!"


# Примеры использования
if __name__ == "__main__":
    # Тестовые случаи из задания
    print(verify_card_number("453914889"))           # VALID!
    print(verify_card_number("4111-1111-1111-1111")) # VALID!
    print(verify_card_number("453914881"))           # INVALID!
    print(verify_card_number("1234 5678 9012 3456")) # INVALID!
    
    # Дополнительные тесты
    print(verify_card_number("5555 5555 5555 4444")) # VALID! (MasterCard тестовая)
    print(verify_card_number("3782 8224 6310 005"))  # VALID! (Amex)
    print(verify_card_number("1234 5678 9012 3456")) # INVALID!