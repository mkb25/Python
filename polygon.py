import math

class Rectangle:
    def __init__(self,width,height):
        self.height = height
        self.width = width

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

    def set_height(self,val):
        self.height = val
    
    def set_width(self,val):
        self.width = val

    def get_area(self):
        return self.height*self.width
    
    def get_perimeter(self):
        return 2*(self.height+self.width)

    def get_diagonal(self):
        return math.sqrt(self.height**2 + self.width**2)

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        return (("*" * self.width) + "\n") * self.height

    def get_amount_inside(self, shape):
        # Calculate how many times the passed shape's width/height 
        # fits into this shape's width/height (floor division)
        horizontal_fit = self.width // shape.width
        vertical_fit = self.height // shape.height
        return horizontal_fit * vertical_fit

class Square(Rectangle):
    def __init__(self,side):
        super().__init__(side, side)

    def __str__(self):
        return f"Square(side={self.width})"

    def set_height(self,val):
        self.height = val
    
    def set_width(self,val):
        self.width = val

    def get_side(self,side):
        self.height = side
        self.width = side
        
rect = Rectangle(10, 5)
sq = Square(8)
print(sq)
print(rect)
print(sq.get_picture())
print(rect.get_diagonal())
print(rect.get_picture())