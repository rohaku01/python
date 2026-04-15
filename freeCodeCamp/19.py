class SimpleCache:
    def __init__(self, maxsize=5):
        self.maxsize = maxsize
        self.cache = {}
        self.freq = {}
    
    def get(self, key):
        if key in self.cache:
            self.freq[key] = self.freq.get(key, 0) + 1
            return self.cache[key]
        return None
    
    def put(self, key, value):
        # Если ключ уже есть — обновляем значение
        if key in self.cache:
            self.cache[key] = value
            self.freq[key] = self.freq.get(key, 0) + 1
            return
        
        # Если кэш полон — удаляем наименее часто используемый
        if len(self.cache) >= self.maxsize:
            # Находим ключ с наименьшей частотой
            lfu_key = min(self.freq.items(), key=lambda x: x[1])[0]
            del self.cache[lfu_key]
            del self.freq[lfu_key]
        
        # Добавляем новый элемент
        self.cache[key] = value
        self.freq[key] = 1
    
    def clear(self):
        self.cache.clear()
        self.freq.clear()
    
    def __len__(self):
        return len(self.cache)
    
    def __str__(self):
        return f"Cache: {self.cache}"
    
cache = SimpleCache(maxsize=3)

cache.put("a", 1)
cache.put("b", 2)
cache.put("c", 3)
print(cache)  # Cache: {'a': 1, 'b': 2, 'c': 3}

cache.get("a")
cache.get("a")
cache.get("b")

cache.put("d", 4)  # удалит "c" (freq=0)
print(cache)  # Cache: {'a': 1, 'b': 2, 'd': 4}

print(cache.get("c"))  # None

print(len(cache))  # 3

cache.clear()
print(cache)  # Cache: {}