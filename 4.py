my_set = {1,2,3,4,5,6,7,8,9,10}
myset = {1,2,3,4,5,6,7,8,9,89}
my_set2 = {"a","b","c","d","e","f","g"}
print(my_set)
print(type(my_set))
print(my_set2 | my_set)
print(my_set.union(my_set2))
print(my_set-myset)
print(my_set^myset)
print(myset.isdisjoint(my_set2))
products = {
    'Laptop': 990,
    'Smartphone': 600,
    'Tablet': 250,
    'Headphones': 70,
}

for product in products.items():
    print(product)

class Shape:
    def area(self):
        pass
class Rectangle(Shape):
    def __init__(self,width,height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius * self.radius
    
shapes = [Rectangle(5,10),Circle(7)]
my_shape = Shape()
print(my_shape)
for shape in shapes:
    print(f'{shape.__class__.__name__}: {shape.area()}')

from abc import ABC,abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
class Rectangle1(Shape):
    def __init__(self,width,height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
class Circle1(Shape):
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius * self.radius
    
shapes = [Rectangle1(5,6),Circle1(9)]
myShape=Shape()
for shape in shapes:
    print(f'{shape.__class__.__name__}: {shape.area()}')