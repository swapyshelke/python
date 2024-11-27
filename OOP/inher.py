class Shape:
    def __init__(self, color, is_filled):
        self.color = color 
        self.is_filled = is_filled
    
class Circle(Shape):
    def __init__(self, color, is_filled, radius):
        super().__init__(color, is_filled)
        self.radius = radius


class Triangle(Shape):
    def __init__(self, color, is_filled, base, height):
        super().__init__(color, is_filled)
        self.base = base 
        self.height = height

    
    
class Rectangle(Shape):
    def __init__(self, color, is_filled, len, breadth):
        super().__init__(color, is_filled)
        self.len = len 
        self.breadth = breadth
        
shape1 = Rectangle("red", False, 10, 20)

print(shape1.color)
print(shape1.is_filled)
print(shape1.len)
print(shape1.breadth)
        