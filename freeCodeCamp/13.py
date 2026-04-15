from abc import ABC, abstractmethod
from typing import List

class Product:
    """Класс продукта с названием и ценой."""
    
    def __init__(self, name: str, price: float) -> None:
        if price < 0:
            raise ValueError("Price cannot be negative")
        self.name = name
        self.price = price

    def __str__(self) -> str:
        return f'{self.name} - ${self.price:.2f}'


class DiscountStrategy(ABC):
    """Абстрактный базовый класс для стратегий скидок."""
    
    @abstractmethod
    def is_applicable(self, product: Product, user_tier: str) -> bool:
        """Проверяет, применима ли скидка."""
        pass

    @abstractmethod
    def apply_discount(self, product: Product) -> float:
        """Применяет скидку и возвращает новую цену."""
        pass


class PercentageDiscount(DiscountStrategy):
    """Скидка в процентах от цены."""
    
    MAX_PERCENT = 70
    
    def __init__(self, percent: int) -> None:
        if percent < 0 or percent > self.MAX_PERCENT:
            raise ValueError(f"Percent must be between 0 and {self.MAX_PERCENT}")
        self.percent = percent

    def is_applicable(self, product: Product, user_tier: str) -> bool:
        return self.percent <= self.MAX_PERCENT

    def apply_discount(self, product: Product) -> float:
        discounted = product.price * (1 - self.percent / 100)
        return max(0, discounted)  # не может быть отрицательной


class FixedAmountDiscount(DiscountStrategy):
    """Фиксированная скидка в денежном выражении."""
    
    MIN_PRICE_THRESHOLD = 0.9  # 90% от цены
    
    def __init__(self, amount: float) -> None:
        if amount < 0:
            raise ValueError("Amount cannot be negative")
        self.amount = amount

    def is_applicable(self, product: Product, user_tier: str) -> bool:
        # Скидка применима, если цена со скидкой больше 90% от исходной
        return product.price * self.MIN_PRICE_THRESHOLD > self.amount

    def apply_discount(self, product: Product) -> float:
        discounted = product.price - self.amount
        return max(0, discounted)  # не может быть отрицательной


class PremiumUserDiscount(DiscountStrategy):
    """Скидка для премиум-пользователей."""
    
    def __init__(self, discount_percent: int = 20) -> None:
        self.discount_percent = discount_percent

    def is_applicable(self, product: Product, user_tier: str) -> bool:
        return user_tier.lower() == 'premium'

    def apply_discount(self, product: Product) -> float:
        return product.price * (1 - self.discount_percent / 100)


class DiscountEngine:
    """Движок для вычисления лучшей цены с применением стратегий скидок."""
    
    def __init__(self, strategies: List[DiscountStrategy]) -> None:
        self.strategies = strategies

    def calculate_best_price(self, product: Product, user_tier: str) -> float:
        """
        Вычисляет лучшую (минимальную) цену после применения всех применимых скидок.
        
        Args:
            product: Объект продукта
            user_tier: Уровень пользователя (обычный, премиум и т.д.)
            
        Returns:
            float: Лучшая цена после применения скидок
        """
        prices = [product.price]

        for strategy in self.strategies:
            if strategy.is_applicable(product, user_tier):
                discounted = strategy.apply_discount(product)
                prices.append(discounted)

        return min(prices)


if __name__ == '__main__':
    product = Product('Wireless Mouse', 50.0)
    user_tier = 'Premium'

    strategies = [
        PercentageDiscount(10),
        FixedAmountDiscount(5),
        PremiumUserDiscount(20)
    ]

    engine = DiscountEngine(strategies)
    best_price = engine.calculate_best_price(product, user_tier)
    
    print(f"Best price for {product.name} for {user_tier} user: ${best_price:.2f}")
    print(f"Original price: ${product.price:.2f}")
    print(f"Saved: ${product.price - best_price:.2f}")