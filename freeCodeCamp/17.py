class LinkedList:
    """Односвязный список."""
    
    class Node:
        """Внутренний класс узла списка."""
        
        def __init__(self, element):
            self.element = element
            self.next = None
    
    def __init__(self):
        self.length = 0
        self.head = None
    
    def is_empty(self) -> bool:
        """Проверяет, пуст ли список."""
        return self.length == 0
    
    def add(self, element) -> None:
        """Добавляет элемент в конец списка."""
        node = self.Node(element)
        if self.is_empty():
            self.head = node
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = node
        self.length += 1
    
    def remove(self, element) -> bool:
        """
        Удаляет первый найденный элемент.
        
        Returns:
            bool: True если элемент удален, False если не найден
        """
        previous_node = None
        current_node = self.head
        
        while current_node is not None and current_node.element != element:
            previous_node = current_node
            current_node = current_node.next
        
        if current_node is None:
            return False
        
        if previous_node is None:
            self.head = current_node.next
        else:
            previous_node.next = current_node.next
        
        self.length -= 1
        return True
    
    def search(self, element) -> bool:
        """Проверяет, есть ли элемент в списке."""
        current_node = self.head
        while current_node is not None:
            if current_node.element == element:
                return True
            current_node = current_node.next
        return False
    
    def __str__(self) -> str:
        """Строковое представление списка."""
        if self.is_empty():
            return "[]"
        
        elements = []
        current_node = self.head
        while current_node is not None:
            elements.append(str(current_node.element))
            current_node = current_node.next
        return "[" + " -> ".join(elements) + "]"


# Тестирование
my_list = LinkedList()
print(my_list.is_empty())  # True

my_list.add(1)
my_list.add(2)
my_list.add(3)
print(my_list)              # [1 -> 2 -> 3]
print(my_list.is_empty())   # False
print(my_list.length)       # 3

my_list.remove(2)
print(my_list)              # [1 -> 3]
print(my_list.length)       # 2

print(my_list.search(1))    # True
print(my_list.search(5))    # False