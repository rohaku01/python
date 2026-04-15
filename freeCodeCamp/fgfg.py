class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        return f'{self.name} makes a sound: {self.bark}'

class Dog(Animal):
    bark = 'woof! woof!! woof!!!'

jack = Dog('Jack')
print(jack.sound())  # Jack makes a sound
print(jack.bark)  # woof! woof!! woof!!!