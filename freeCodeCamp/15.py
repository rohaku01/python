import math
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def set_width(self, new_width):
        self.width = new_width
    def set_height(self, new_height):
        self.height = new_height
    def get_area(self):
        return self.width * self.height
    def get_perimeter(self):
        return 2 * (self.width + self.height)
    def get_diagonal(self):
        return math.sqrt(pow(self.width,2) + pow(self.height, 2))
    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return 'Too big for picture.'
    
        picture = ''
        for _ in range(self.height):
            picture += '*' * self.width + '\n'
        return picture
    def get_amount_inside(self, figure):
        width_fit = self.width // figure.width
        height_fit = self.height // figure.height
        return width_fit * height_fit
    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"
class Square(Rectangle):
    def __init__(self,side):
        super().__init__(side, side)
        self.side = side
    def set_width(self, width):
        self.side = width
        self.width = width
        self.height = width
    
    def set_height(self, height):
        self.side = height
        self.width = height
        self.height = height
    
    def set_side(self, side):
        self.side = side
        self.width = side
        self.height = side
    def __str__(self):
        return f"Square(side={self.side})"
    

    