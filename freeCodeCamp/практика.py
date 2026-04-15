from datetime import datetime, timedelta
class StoreError(Exception):
    """Ошибки искл в магазине"""
    def __init__(self, message, obj):
        super().__init__(message)
        self.obj = obj
class Product:
    def __init__(self, name: str, price: float, sku: str):
        if not name.strip():
            raise ValueError('НАЗВ НЕ ДОЛЖНО БЫТЬ ПУСТЫМ')
        if price < 0:
            raise ValueError('цена должна быть больше 0')
        sku_str = str(sku)
        if sku_str.isdigit() != 8:
            raise ValueError('арт из 8 цифр')
        self.name = name
        self.price = price
        self._original_price = price
        self.discount = 0
    def apply_discount(self, percent):
        if 0 < percent < 100:
            self.discount = percent
            self.price = self._original_price * (1 - percent / 100)
            return True
        return False
    def remove_discount(self):
        self.discount = 0
        self.price = self._original_price
    def __str__(self):
        if self.discount > 0:
            return f"{self.name} - Цена: {self.price:.2f} руб. (скидка {self.discount}%) (SKU: {self.sku})"
        return f"{self.name} - Цена: {self.price:.2f} руб. (SKU: {self.sku})"
class Electronics(Product):
    def __init__(self, name, price, sku, warranty_month: int, brand: str):
        if  warranty_month < 1 or warranty_month > 36:
            raise ValueError('гарантия от 1 до 36 мес')
        if not brand.strip():
            raise ValueError('бред не должен быть пустой')
        super().__init__(name, price, sku)
        self.warranty_month = warranty_month
        self.brand = brand
    def __str__(self):
        base = super().__str__()
        return f"{base} [{self.brand}, гарантия {self.warranty_month} мес.]"
class Clothing(Product):
    VALID_SIZE = {'S', 'M', 'L', 'XL', 'XXL'}
    def __init__(self, name, price, sku, size: str, material: str):
        if size not in self.VALID_SIZE:
            raise ValueError('Размер не допустим, выберите из (S, M, L, XL, XXL)')
        if not material.strip():
            raise ValueError('материал не может быть пуст')
        super().__init__(name ,price, sku)
        self.size = size
        self.material = material
    def __str__(self):
        base = super().__str__()
        return f"{base} [Размер {self.size}, {self.material}]"
class Book(Product):
    def __init__(self, name, price, sku, author: str, pages: int):
        if not author.strip():
            raise ValueError('автор не должен быть пустой')
        if pages <= 0 :
            raise ValueError('страниц должно быть больше 0')
        super().__init__(name ,price, sku)
        self.author = author
        self.pages = pages
    def __str__(self):
        base = super().__init__(self)
        return f"{base} [{self.author}, {self.pages} стр.]"
class Store:
    def __init__(self):
        self.products = []
        self.sales = []
    def add_product(self, product):
        if not isinstance(product, Product):
            raise StoreError('объект не класса продукт')
        self.products.append(product)
    def remove_product(self, sku):
        for i,p in enumerate(self.products):
            if p.sku == sku:
                for s in self.sales:
                    if p in self.sales:
                        s.remove_product(p)
                return self.products.pop(i)
        return None
    def add_sale(self, sale):
        """Добавляет акцию в магазин"""
        self.sales.append(sale)
        return True
    def get_electronics(self):
        """Возвращает список электроники"""
        return [p for p in self.products if isinstance(p, Electronics)]
    
    def get_clothing(self):
        """Возвращает список одежды"""
        return [p for p in self.products if isinstance(p, Clothing)]
    
    def get_books(self):
        """Возвращает список книг"""
        return [p for p in self.products if isinstance(p, Book)]
    
    def get_bundles(self):
        """Возвращает списки наборов"""
        return [p for p in self.products if isinstance(p, Bundle)]
    
    def search_by_price(self, min_price, max_price):
        """Поиск по диапазону цен"""
        return [p for p in self.products if min_price <= p.price <= max_price]
    
    def search_by_brand(self, brand):
        """Поиск электроники по бренду"""
        return [p for p in self.products if isinstance(p, Electronics) and p.brand == brand]
    def searhc_by_author(self, author):
        return [p for p in self.products if isinstance(p, Book) and author.lower() in p.author.lower()]
    def sort_by_price(self, ascending=True):
        self.products.sort(key=lambda p: p.price, reverse =  not ascending)
    def sort_by_name(self, ascending=True):
        self.products.sort(key=lambda p: p.name, reverse=not ascending)
    def get_most_expansive(self, n=1):
        if not self.products:
            return []
        sorted_products = sorted(self.products, key=lambda p: p.price, reverse=True)
        return sorted_products[:n]
    def get_cheapest(self, n=1):
        if not self.products:
            return []
        sorted_products = sorted(self.products, key=lambda p: p.price, reverse=False)
        return sorted_products[:n]
    def get_statistics(self):
        """Возвращает статистику по магазину"""
        if not self.products:
            return {
                'total': 0,
                'avg_price': 0,
                'total_value': 0,
                'most_expensive': None,
                'cheapest': None,
                'by_category': {'electronics': 0, 'clothing': 0, 'books': 0, 'bundles': 0}
            }
        total_value = sum(p.price for p in self.products)
        av_value = total_value / len(self.products)
        return {
                'total': len(self.products),
                'avg_price': av_value,
                'total_value': total_value,
                'most_expensive': max(self.products, key=lambda p: p.price),
                'cheapest': min(self.products, key=lambda p: p.price),
                'by_category': {'electronics': len(self.get_electronics()),
                                'clothing': len(self.get_clothing()),
                                'books': len(self.get_books()),
                                'bundles': len(self.get_bundles())}
        }
    def __str__(self):
        result = f"🏪 МАГАЗИН (Всего товаров: {len(self.products)})\n"
        result += "=" * 60 + "\n\n"
        
        # Электроника
        result += "📱 ЭЛЕКТРОНИКА\n"
        result += "-" * 40 + "\n"
        electronics = self.get_electronics()
        if electronics:
            for i, item in enumerate(electronics, 1):
                result += f"{i}. {item}\n"
        else:
            result += "Нет товаров\n"
        
        result += "\n"
        
        # Одежда
        result += "👕 ОДЕЖДА\n"
        result += "-" * 40 + "\n"
        clothing = self.get_clothing()
        if clothing:
            for i, item in enumerate(clothing, 1):
                result += f"{i}. {item}\n"
        else:
            result += "Нет товаров\n"
        
        result += "\n"
        
        # Книги
        result += "📚 КНИГИ\n"
        result += "-" * 40 + "\n"
        books = self.get_books()
        if books:
            for i, item in enumerate(books, 1):
                result += f"{i}. {item}\n"
        else:
            result += "Нет товаров\n"
        
        result += "\n"
        
        # Наборы
        result += "🎁 НАБОРЫ\n"
        result += "-" * 40 + "\n"
        bundles = self.get_bundles()
        if bundles:
            for i, item in enumerate(bundles, 1):
                result += f"{i}. {item}\n"
        else:
            result += "Нет наборов\n"
        
        return result
class Sale:
    def __init__(self, name, discount_percent, start_date=None, end_date=None):
        self.name = name
        self.discount_percent = discount_percent
        self.start_date = start_date or datetime.now()
        self.end_date = end_date or (self.start_date + timedelta(days=30))
        self.products = []
    def add_product(self,product):
        if product in self.products:
            return False
        self.products.append(product)
        product.apply_discount(self.discount_percent)
    def remove_product(self, product):
        if product in self.products:
            self.products.remove(product)
            product.remove_discount()
            return True
        return False
    def is_active(self):
        """Проверяет, активна ли акция"""
        now = datetime.now()
        return self.start_date <= now <= self.end_date
    
    def __str__(self):
        status = "Активна" if self.is_active() else "Завершена"
        return f"Акция '{self.name}': {self.discount_percent}% | Статус: {status} | Товаров: {len(self.products)}"
class Bundle(Product):
    def __init__(self, name,products, bundle_discount=10):
        
        total_price = sum(p.price for p in products)
        sku = f"BUNDLE_{hash(name) % 100000000:08d}"
        
        super().__init__(name, total_price, sku)
        self.products = products
        self.bundle_discount = bundle_discount
        self._original_price = total_price
        
        # Применяем скидку набора
        self.apply_discount(bundle_discount)
    
    def __str__(self):
        base = super().__str__()
        products_str = ', '.join(p.name for p in self.products)
        return f"{base} [Набор: {products_str}]"
    
    def get_individual_prices(self):
        """Возвращает цены отдельных товаров"""
        return {p.name: p.price for p in self.products}
        
