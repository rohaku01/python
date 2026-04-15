from datetime import datetime, timedelta
import random


# ============================================
# ПОЛЬЗОВАТЕЛЬСКИЕ ИСКЛЮЧЕНИЯ
# ============================================

class StoreError(Exception):
    """Пользовательские исключения для ошибок магазина"""
    def __init__(self, message, obj):
        super().__init__(message)
        self.obj = obj


# ============================================
# БАЗОВЫЙ КЛАСС PRODUCT
# ============================================

class Product:
    def __init__(self, name, price, sku):
        if not name.strip():
            raise ValueError('Название не должно быть пустым')
        if price <= 0:
            raise ValueError('Цена должна быть больше 0')
        
        sku_str = str(sku)
        if not sku_str.isdigit() or len(sku_str) != 8:
            raise ValueError('Артикул должен быть из 8 цифр')
        
        self.name = name
        self._original_price = price
        self.price = price
        self.sku = sku_str
        self.discount = 0  # текущая скидка в процентах
    
    def apply_discount(self, percent):
        """
        Применяет скидку к товару.
        
        Args:
            percent: процент скидки (0-100)
        """
        if not 0 <= percent <= 100:
            raise ValueError('Скидка должна быть от 0 до 100%')
        
        self.discount = percent
        self.price = self._original_price * (1 - percent / 100)
        return self.price
    
    def remove_discount(self):
        """Убирает скидку"""
        self.discount = 0
        self.price = self._original_price
    
    def __str__(self):
        if self.discount > 0:
            return f"{self.name} - Цена: {self.price:.2f} руб. (скидка {self.discount}%) (SKU: {self.sku})"
        return f"{self.name} - Цена: {self.price:.2f} руб. (SKU: {self.sku})"


# ============================================
# КЛАСС ЭЛЕКТРОНИКА
# ============================================

class Electronics(Product):
    def __init__(self, name, price, sku, warranty_month, brand):
        if warranty_month < 1 or warranty_month > 36:
            raise ValueError('Гарантия должна быть 1-36 месяцев')
        if not brand.strip():
            raise ValueError('Бренд не может быть пустым')
        
        super().__init__(name, price, sku)
        self.warranty_month = warranty_month
        self.brand = brand
    
    def __str__(self):
        base = super().__str__()
        return f"{base} [{self.brand}, гарантия {self.warranty_month} мес.]"


# ============================================
# КЛАСС ОДЕЖДА
# ============================================

class Clothing(Product):
    VALID_SIZES = {'S', 'M', 'L', 'XL', 'XXL'}
    
    def __init__(self, name, price, sku, size, material):
        if size not in self.VALID_SIZES:
            raise ValueError(f'Размер должен быть одним из: {", ".join(self.VALID_SIZES)}')
        if not material.strip():
            raise ValueError('Материал не может быть пустым')
        
        super().__init__(name, price, sku)
        self.size = size
        self.material = material
    
    def __str__(self):
        base = super().__str__()
        return f"{base} [Размер {self.size}, {self.material}]"


# ============================================
# КЛАСС КНИГА
# ============================================

class Book(Product):
    def __init__(self, name, price, sku, author, pages):
        if not author.strip():
            raise ValueError('Автор не должен быть пустым')
        if pages <= 0:
            raise ValueError('Страниц должно быть больше 0')
        
        super().__init__(name, price, sku)
        self.author = author
        self.pages = pages
    
    def __str__(self):
        base = super().__str__()
        return f"{base} [{self.author}, {self.pages} стр.]"


# ============================================
# КЛАСС НАБОР ТОВАРОВ
# ============================================

class Bundle(Product):
    """Набор товаров со скидкой"""
    
    def __init__(self, name, products, bundle_discount=10):
        """
        Args:
            name: название набора
            products: список товаров в наборе
            bundle_discount: дополнительная скидка на набор (%)
        """
        # Вычисляем общую стоимость
        total_price = sum(p.price for p in products)
        # Генерируем SKU на основе имени
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


# ============================================
# КЛАСС АКЦИЯ
# ============================================

class Sale:
    """Управление акциями в магазине"""
    
    def __init__(self, name, discount_percent, start_date=None, end_date=None):
        self.name = name
        self.discount_percent = discount_percent
        self.start_date = start_date or datetime.now()
        self.end_date = end_date or (self.start_date + timedelta(days=30))
        self.products = []  # товары, участвующие в акции
    
    def add_product(self, product):
        """Добавляет товар в акцию"""
        if product not in self.products:
            self.products.append(product)
            product.apply_discount(self.discount_percent)
            return True
        return False
    
    def remove_product(self, product):
        """Удаляет товар из акции"""
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


# ============================================
# КЛАСС МАГАЗИН
# ============================================

class Store:
    def __init__(self):
        self.products = []
        self.sales = []  # список акций
    
    def add_product(self, product):
        """Добавляет товар в магазин"""
        if not isinstance(product, Product):
            raise StoreError('Можно добавлять только экземпляры Product или его наследников', product)
        self.products.append(product)
        return True
    
    def remove_product(self, sku):
        """Удаляет товар по артикулу"""
        for i, product in enumerate(self.products):
            if product.sku == sku:
                # Удаляем из акций, если участвует
                for sale in self.sales:
                    if product in sale.products:
                        sale.remove_product(product)
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
    
    def search_by_author(self, author):
        """Поиск книг по автору"""
        return [p for p in self.products if isinstance(p, Book) and author.lower() in p.author.lower()]
    
    def sort_by_price(self, ascending=True):
        """Сортирует товары по цене"""
        self.products.sort(key=lambda p: p.price, reverse=not ascending)
    
    def sort_by_name(self, ascending=True):
        """Сортирует товары по названию"""
        self.products.sort(key=lambda p: p.name.lower(), reverse=not ascending)
    
    def get_most_expensive(self, n=1):
        """Возвращает n самых дорогих товаров"""
        if not self.products:
            return []
        sorted_products = sorted(self.products, key=lambda p: p.price, reverse=True)
        return sorted_products[:n]
    
    def get_cheapest(self, n=1):
        """Возвращает n самых дешевых товаров"""
        if not self.products:
            return []
        sorted_products = sorted(self.products, key=lambda p: p.price)
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
        avg_price = total_value / len(self.products)
        
        return {
            'total': len(self.products),
            'avg_price': avg_price,
            'total_value': total_value,
            'most_expensive': max(self.products, key=lambda p: p.price),
            'cheapest': min(self.products, key=lambda p: p.price),
            'by_category': {
                'electronics': len(self.get_electronics()),
                'clothing': len(self.get_clothing()),
                'books': len(self.get_books()),
                'bundles': len(self.get_bundles())
            }
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


# ============================================
# ДЕМОНСТРАЦИЯ РАБОТЫ
# ============================================

def print_header(title):
    """Выводит красивый заголовок"""
    print("\n" + "=" * 70)
    print(f"{title:^70}")
    print("=" * 70)


if __name__ == "__main__":
    store = Store()
    
    try:
        # ============================================
        # СОЗДАНИЕ ТОВАРОВ
        # ============================================
        print_header("📦 СОЗДАНИЕ ТОВАРОВ")
        
        laptop = Electronics("MacBook Pro 14", 150000, "12345678", 24, "Apple")
        phone = Electronics("iPhone 15 Pro", 95000, "87654321", 12, "Apple")
        headphones = Electronics("Sony WH-1000XM5", 35000, "11223344", 24, "Sony")
        
        tshirt = Clothing("Футболка", 1500, "44332211", "L", "Хлопок")
        jacket = Clothing("Куртка", 5000, "55667788", "XL", "Кожа")
        jeans = Clothing("Джинсы", 3000, "66778899", "M", "Деним")
        
        book1 = Book("Война и мир", 800, "99887766", "Л.Н. Толстой", 1300)
        book2 = Book("Преступление и наказание", 650, "88776655", "Ф.М. Достоевский", 670)
        book3 = Book("Мастер и Маргарита", 700, "77665544", "М.А. Булгаков", 480)
        
        print("✅ Товары созданы успешно")
        
        # ============================================
        # ДОБАВЛЕНИЕ В МАГАЗИН
        # ============================================
        print_header("🏪 ДОБАВЛЕНИЕ В МАГАЗИН")
        
        for product in [laptop, phone, headphones, tshirt, jacket, jeans, book1, book2, book3]:
            store.add_product(product)
        
        print(f"✅ Добавлено товаров: {len(store.products)}")
        
        # ============================================
        # ПРИМЕНЕНИЕ СКИДКИ
        # ============================================
        print_header("💰 ПРИМЕНЕНИЕ СКИДКИ (ЗАДАНИЕ 1)")
        
        print(f"\nДо скидки: {laptop}")
        laptop.apply_discount(15)
        print(f"После скидки 15%: {laptop}")
        laptop.remove_discount()
        print(f"После удаления скидки: {laptop}")
        
        # ============================================
        # АКЦИИ
        # ============================================
        print_header("🎉 АКЦИИ (ЗАДАНИЕ 2)")
        
        summer_sale = Sale("Летняя распродажа", 20)
        summer_sale.add_product(tshirt)
        summer_sale.add_product(jeans)
        summer_sale.add_product(headphones)
        store.add_sale(summer_sale)
        
        print(f"\n{summer_sale}")
        print("\nТовары в акции:")
        for product in summer_sale.products:
            print(f"   • {product}")
        
        # ============================================
        # СОРТИРОВКА
        # ============================================
        print_header("📊 СОРТИРОВКА (ЗАДАНИЕ 3)")
        
        print("\nСортировка по цене (от дешевых к дорогим):")
        store.sort_by_price(ascending=True)
        for i, p in enumerate(store.products[:5], 1):
            print(f"   {i}. {p.name}: {p.price:.2f} руб.")
        
        print("\nСортировка по названию (по алфавиту):")
        store.sort_by_name(ascending=True)
        for i, p in enumerate(store.products[:5], 1):
            print(f"   {i}. {p.name}")
        
        # ============================================
        # НАБОРЫ ТОВАРОВ
        # ============================================
        print_header("🎁 НАБОРЫ ТОВАРОВ (ЗАДАНИЕ 4)")
        
        student_bundle = Bundle("Студенческий набор", [book2, tshirt, headphones], bundle_discount=15)
        store.add_product(student_bundle)
        
        print(f"\n{student_bundle}")
        print(f"\nОтдельные цены в наборе:")
        for name, price in student_bundle.get_individual_prices().items():
            print(f"   • {name}: {price:.2f} руб.")
        
        # ============================================
        # САМЫЕ ДОРОГИЕ ТОВАРЫ
        # ============================================
        print_header("💎 САМЫЕ ДОРОГИЕ ТОВАРЫ (ЗАДАНИЕ 5)")
        
        top_expensive = store.get_most_expensive(5)
        print("\nТоп-5 самых дорогих товаров:")
        for i, product in enumerate(top_expensive, 1):
            print(f"   {i}. {product.name}: {product.price:.2f} руб.")
        
        # ============================================
        # ПОИСК
        # ============================================
        print_header("🔍 ПОИСК ТОВАРОВ")
        
        print("\nПоиск по цене (1000 - 50000 руб.):")
        found = store.search_by_price(1000, 50000)
        for product in found[:5]:
            print(f"   • {product.name}: {product.price:.2f} руб.")
        
        print("\nПоиск по бренду (Apple):")
        found = store.search_by_brand("Apple")
        for product in found:
            print(f"   • {product.name}: {product.price:.2f} руб.")
        
        print("\nПоиск книг по автору (Достоевский):")
        found = store.search_by_author("Достоевский")
        for product in found:
            print(f"   • {product}")
        
        # ============================================
        # СТАТИСТИКА
        # ============================================
        print_header("📊 СТАТИСТИКА МАГАЗИНА")
        
        stats = store.get_statistics()
        print(f"\n📦 Всего товаров: {stats['total']}")
        print(f"💰 Средняя цена: {stats['avg_price']:.2f} руб.")
        print(f"💵 Общая стоимость: {stats['total_value']:.2f} руб.")
        print(f"\n📱 Электроника: {stats['by_category']['electronics']}")
        print(f"👕 Одежда: {stats['by_category']['clothing']}")
        print(f"📚 Книги: {stats['by_category']['books']}")
        print(f"🎁 Наборы: {stats['by_category']['bundles']}")
        
        if stats['most_expensive']:
            print(f"\n🏆 Самый дорогой: {stats['most_expensive'].name} ({stats['most_expensive'].price:.2f} руб.)")
        if stats['cheapest']:
            print(f"🎯 Самый дешевый: {stats['cheapest'].name} ({stats['cheapest'].price:.2f} руб.)")
        
        # ============================================
        # ВЫВОД ВСЕГО МАГАЗИНА
        # ============================================
        print_header("🏪 ПОЛНЫЙ КАТАЛОГ МАГАЗИНА")
        print("\n" + str(store))
        
        # ============================================
        # ЗАВЕРШЕНИЕ
        # ============================================
        print_header("✨ РАБОТА МАГАЗИНА УСПЕШНО ЗАВЕРШЕНА")
        print("\n✅ Все задания выполнены!")
        print("✅ Классы работают корректно!")
        print("✅ Дополнительные функции реализованы!")
        print("\n" + "=" * 70)
        
    except ValueError as e:
        print(f"\n❌ Ошибка валидации: {e}")
    except StoreError as e:
        print(f"\n❌ Ошибка магазина: {e}")
        print(f"   Объект: {e.obj}")
    except Exception as e:
        print(f"\n❌ Непредвиденная ошибка: {e}")