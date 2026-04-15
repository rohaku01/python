class GameCharacter:
    """
    Класс игрового персонажа с системой уровня, здоровья и маны.
    
    Attributes:
        name (str): Имя персонажа
        health (int): Текущее здоровье (0-100)
        mana (int): Текущая мана (0-50)
        level (int): Текущий уровень (начинается с 1)
    """
    
    # Константы класса
    MAX_HEALTH = 100
    MAX_MANA = 50
    START_HEALTH = 100
    START_MANA = 50
    START_LEVEL = 1
    
    def __init__(self, name: str) -> None:
        """
        Инициализация нового персонажа.
        
        Args:
            name: Имя персонажа
            
        Raises:
            TypeError: Если name не является строкой
        """
        if not isinstance(name, str):
            raise TypeError("Name must be a string")
        
        self._name = name
        self._health = self.START_HEALTH
        self._mana = self.START_MANA
        self._level = self.START_LEVEL
    
    @property
    def name(self) -> str:
        """
        Геттер имени персонажа.
        
        Returns:
            str: Имя персонажа
        """
        return self._name
    
    @property
    def health(self) -> int:
        """
        Геттер здоровья персонажа.
        
        Returns:
            int: Текущее здоровье (0-100)
        """
        return self._health
    
    @health.setter
    def health(self, new_health: int) -> None:
        """
        Сеттер здоровья с ограничением от 0 до MAX_HEALTH.
        
        Args:
            new_health: Новое значение здоровья
        """
        if new_health < 0:
            self._health = 0
            print(f"⚠️ {self._name} упал в обморок!")
        elif new_health > self.MAX_HEALTH:
            self._health = self.MAX_HEALTH
            print(f"✨ {self._name} полностью восстановил здоровье!")
        else:
            self._health = new_health
    
    @property
    def mana(self) -> int:
        """
        Геттер маны персонажа.
        
        Returns:
            int: Текущая мана (0-50)
        """
        return self._mana
    
    @mana.setter
    def mana(self, new_mana: int) -> None:
        """
        Сеттер маны с ограничением от 0 до MAX_MANA.
        
        Args:
            new_mana: Новое значение маны
        """
        if new_mana < 0:
            self._mana = 0
            print(f"⚠️ {self._name} истощил свою ману!")
        elif new_mana > self.MAX_MANA:
            self._mana = self.MAX_MANA
            print(f"✨ {self._name} восстановил всю ману!")
        else:
            self._mana = new_mana
    
    @property
    def level(self) -> int:
        """
        Геттер уровня персонажа.
        
        Returns:
            int: Текущий уровень
        """
        return self._level
    
    def level_up(self) -> None:
        """
        Повышает уровень персонажа на 1.
        Восстанавливает здоровье и ману до максимума.
        """
        old_level = self._level
        self._level += 1
        self.health = self.MAX_HEALTH
        self.mana = self.MAX_MANA
        print(f"🎉 {self._name} повысил уровень с {old_level} до {self._level}! 🎉")
    
    def take_damage(self, damage: int) -> None:
        """
        Наносит урон персонажу.
        
        Args:
            damage: Количество урона
        """
        if damage < 0:
            raise ValueError("Damage cannot be negative")
        
        self.health -= damage
        print(f"💔 {self._name} получил {damage} урона! Осталось здоровья: {self.health}")
    
    def heal(self, amount: int) -> None:
        """
        Лечит персонажа.
        
        Args:
            amount: Количество лечения
        """
        if amount < 0:
            raise ValueError("Heal amount cannot be negative")
        
        self.health += amount
        print(f"💚 {self._name} восстановил {amount} здоровья! Теперь здоровья: {self.health}")
    
    def use_mana(self, cost: int) -> bool:
        """
        Использует ману для способности.
        
        Args:
            cost: Стоимость способности в мане
            
        Returns:
            bool: True если маны достаточно, иначе False
        """
        if cost < 0:
            raise ValueError("Mana cost cannot be negative")
        
        if self.mana >= cost:
            self.mana -= cost
            print(f"🔮 {self._name} использовал {cost} маны. Осталось маны: {self.mana}")
            return True
        else:
            print(f"❌ Недостаточно маны! Нужно {cost}, есть {self.mana}")
            return False
    
    def is_alive(self) -> bool:
        """
        Проверяет, жив ли персонаж.
        
        Returns:
            bool: True если здоровье > 0
        """
        return self.health > 0
    
    def __str__(self) -> str:
        """
        Строковое представление персонажа.
        
        Returns:
            str: Отформатированная информация о персонаже
        """
        return (f"Name: {self.name}\n"
                f"Level: {self.level}\n"
                f"Health: {self.health}\n"
                f"Mana: {self.mana}")
    
    def __repr__(self) -> str:
        """
        Представление для отладки.
        
        Returns:
            str: Строка для воссоздания объекта
        """
        return f"GameCharacter('{self.name}')"


# ========== ПРИМЕР ИСПОЛЬЗОВАНИЯ ==========

if __name__ == "__main__":
    # Создаем персонажа
    kratos = GameCharacter("Kratos")
    
    # Выводим информацию
    print("=" * 40)
    print("НОВЫЙ ПЕРСОНАЖ:")
    print(kratos)
    
    # Тестируем урон и лечение
    print("\n" + "=" * 40)
    print("БОЙ:")
    kratos.take_damage(30)
    kratos.take_damage(80)
    kratos.heal(50)
    
    # Тестируем ману
    print("\n" + "=" * 40)
    print("МАГИЯ:")
    kratos.use_mana(20)
    kratos.use_mana(40)
    
    # Повышаем уровень
    print("\n" + "=" * 40)
    print("ПРОКАЧКА:")
    kratos.level_up()
    
    # Проверяем жив ли
    print("\n" + "=" * 40)
    print(f"Жив ли {kratos.name}? {kratos.is_alive()}")
    
    # Финальная информация
    print("\n" + "=" * 40)
    print("ФИНАЛЬНАЯ СТАТИСТИКА:")
    print(kratos)