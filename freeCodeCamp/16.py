class LibraryError(Exception):
    """Пользовательское исключение для ошибок библиотеки."""
    
    def __init__(self, message, obj):
        super().__init__(message)
        self.obj = obj


class Book:
    """Базовый класс для всех книг."""
    
    def __init__(self, title, author, year, isbn):
        if not title.strip():
            raise ValueError('Название не должно быть пустым')
        if not author.strip():
            raise ValueError('Имя автора не может быть пустым')
        if year < 1450:
            raise ValueError('Год должен быть 1450 и более')
        if len(str(isbn)) not in (10, 13) or not str(isbn).isdigit():
            raise ValueError("ISBN должен быть 10 или 13 цифр")
        
        self.title = title
        self.author = author
        self.year = year
        self.isbn = isbn
    
    def __str__(self):
        return f"{self.title} - {self.author} ({self.year}) - ISBN: {self.isbn}"


class EBook(Book):
    """Класс электронной книги."""
    
    def __init__(self, title, author, year, isbn, file_size, file_format):
        if file_size <= 0:
            raise ValueError('Размер файла должен быть больше 0')
        if file_format not in ('pdf', 'epub', 'mobi'):
            raise ValueError("Формат файла должен быть 'pdf', 'epub', 'mobi'")
        
        super().__init__(title, author, year, isbn)
        self.file_size = file_size
        self.file_format = file_format
    
    def __str__(self):
        return f"{self.title} - {self.author} ({self.year}) - ISBN: {self.isbn} [{self.file_format}, {self.file_size} MB]"


class AudioBook(Book):
    """Класс аудиокниги."""
    
    def __init__(self, title, author, year, isbn, duration, narrator):
        if duration <= 0:
            raise ValueError('Продолжительность должна быть больше 0')
        if not narrator.strip():
            raise ValueError('Имя чтеца не может быть пустым')
        
        super().__init__(title, author, year, isbn)
        self.duration = duration
        self.narrator = narrator
    
    def __str__(self):
        hours = self.duration // 60
        minutes = self.duration % 60
        return f"{self.title} - {self.author} ({self.year}) - ISBN: {self.isbn} [{hours}h {minutes}min, narrated by {self.narrator}]"


class Library:
    """Каталог библиотеки."""
    
    def __init__(self):
        self.items = []
    
    def add(self, item):
        if not isinstance(item, Book):
            raise LibraryError('Only Book, EBook or AudioBook instances can be added', item)
        self.items.append(item)
    
    def get_books(self):
        return [b for b in self.items if type(b) is Book]
    
    def get_ebooks(self):
        return [b for b in self.items if isinstance(b, EBook)]
    
    def get_audiobooks(self):
        return [b for b in self.items if isinstance(b, AudioBook)]
    
    def search_by_author(self, author):
        result = [b for b in self.items if author.lower() in b.author.lower()]
        if not result:
            return f"Книги автора {author} не найдены"
        return result
    
    def search_by_year(self, year):
        result = [b for b in self.items if b.year == year]
        if not result:
            return f"Книги {year} года не найдены"
        return result
    
    def __str__(self):
        result = f"Library ({len(self.items)} items):\n\n"
        
        # BOOKS
        books = self.get_books()
        result += "=== BOOKS ===\n"
        if books:
            for i, book in enumerate(books, 1):
                result += f"{i}. {book}\n"
        else:
            result += "No books\n"
        
        result += "\n"
        
        # EBOOKS
        ebooks = self.get_ebooks()
        result += "=== EBOOKS ===\n"
        if ebooks:
            for i, ebook in enumerate(ebooks, 1):
                result += f"{i}. {ebook}\n"
        else:
            result += "No ebooks\n"
        
        result += "\n"
        
        # AUDIOBOOKS
        audiobooks = self.get_audiobooks()
        result += "=== AUDIOBOOKS ===\n"
        if audiobooks:
            for i, audiobook in enumerate(audiobooks, 1):
                result += f"{i}. {audiobook}\n"
        else:
            result += "No audiobooks\n"
        
        return result.rstrip('\n')


if __name__ == "__main__":
    library = Library()
    
    try:
        # Создаем книги
        book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", 1925, "9780141182636")
        book2 = Book("1984", "George Orwell", 1949, "9780451524935")
        book3 = Book("To Kill a Mockingbird", "Harper Lee", 1960, "9780061120084")
        
        ebook1 = EBook("Python Crash Course", "Eric Matthes", 2019, "9781593279288", 5.2, "pdf")
        ebook2 = EBook("Clean Code", "Robert Martin", 2008, "9780132350884", 3.8, "epub")
        ebook3 = EBook("Atomic Habits", "James Clear", 2018, "9780735211292", 2.5, "mobi")
        
        audiobook1 = AudioBook("Harry Potter", "J.K. Rowling", 1997, "9780747532699", 1050, "Stephen Fry")
        audiobook2 = AudioBook("The Hobbit", "J.R.R. Tolkien", 1937, "9780547928227", 660, "Andy Serkis")
        audiobook3 = AudioBook("The Martian", "Andy Weir", 2011, "9780804139021", 660, "R.C. Bray")
        
        # Добавляем в библиотеку
        library.add(book1)
        library.add(book2)
        library.add(book3)
        library.add(ebook1)
        library.add(ebook2)
        library.add(ebook3)
        library.add(audiobook1)
        library.add(audiobook2)
        library.add(audiobook3)
        
        # Выводим библиотеку
        print("=" * 70)
        print("📚 БИБЛИОТЕКА".center(70))
        print("=" * 70)
        print(library)
        
        # Поиск по автору
        print("\n" + "=" * 70)
        print("🔍 ПОИСК ПО АВТОРУ".center(70))
        print("=" * 70)
        
        authors = ["Orwell", "Tolkien", "Rowling", "Unknown"]
        for author in authors:
            print(f"\n📖 Автор: {author}")
            result = library.search_by_author(author)
            if isinstance(result, list):
                for book in result:
                    print(f"   • {book}")
            else:
                print(f"   {result}")
        
        # Поиск по году
        print("\n" + "=" * 70)
        print("📅 ПОИСК ПО ГОДУ".center(70))
        print("=" * 70)
        
        years = [1949, 2019, 2008, 1997, 1960, 2025]
        for year in years:
            print(f"\n📅 Год: {year}")
            result = library.search_by_year(year)
            if isinstance(result, list):
                for book in result:
                    print(f"   • {book}")
            else:
                print(f"   {result}")
        
        # Статистика
        print("\n" + "=" * 70)
        print("📊 СТАТИСТИКА БИБЛИОТЕКИ".center(70))
        print("=" * 70)
        
        print(f"\n📚 Всего книг: {len(library.items)}")
        print(f"📖 Обычных книг: {len(library.get_books())}")
        print(f"💻 Электронных книг: {len(library.get_ebooks())}")
        print(f"🎧 Аудиокниг: {len(library.get_audiobooks())}")
        
        # Самые старые и новые книги
        all_books = library.items
        if all_books:
            oldest = min(all_books, key=lambda b: b.year)
            newest = max(all_books, key=lambda b: b.year)
            print(f"\n🏛️ Самая старая книга: {oldest.title} ({oldest.year})")
            print(f"🆕 Самая новая книга: {newest.title} ({newest.year})")
        
        print("\n" + "=" * 70)
        print("✨ БИБЛИОТЕКА УСПЕШНО ЗАГРУЖЕНА ✨".center(70))
        print("=" * 70)
        
    except ValueError as e:
        print("\n" + "=" * 70)
        print("❌ ОШИБКА ВАЛИДАЦИИ".center(70))
        print("=" * 70)
        print(f"\n⚠️ {e}")
        print("\n" + "=" * 70)
        
    except LibraryError as e:
        print("\n" + "=" * 70)
        print("❌ ОШИБКА БИБЛИОТЕКИ".center(70))
        print("=" * 70)
        print(f"\n⚠️ {e}")
        print(f"📦 Невозможно добавить: {e.obj}")
        print(f"🔍 Тип объекта: {type(e.obj).__name__}")
        print("\n" + "=" * 70)