class HashTable:
    def __init__(self):
        self.collection = {}
    def hash(self, string):
        total = 0
        for char in string:
            total += ord(char)
        return total
    def add(self, key, value):
        hash_value = self.hash(key)
    
        if hash_value not in self.collection:
            self.collection[hash_value] = {}
    
        self.collection[hash_value][key] = value
    def remove(self, key):
        hash_key = self.hash(key)
        if hash_key in self.collection and key in self.collection[hash_key]:
            del self.collection[hash_key][key]
            if not self.collection[hash_key]:
                del self.collection[hash_key]
            return True
        return False
    def lookup(self, key):
        hash_key = self.hash(key)
        if hash_key in self.collection and key in self.collection[hash_key]:
            return self.collection[hash_key][key]
        return None

