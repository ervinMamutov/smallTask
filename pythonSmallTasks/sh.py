""" Modul sh Include class Shape, Square, Circle"""


class Shape:
    """Class Shape: include mothod move"""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, deltaX, deltaY):
        self.x = self.x + deltaX
        self.y = self.y + deltaY


class Square(Shape):
    """Class Square: inherits from Shape"""

    def __init__(self, side=1, x=0, y=0):
        Shape.__init__(self, x, y)
        self.side = side


class Circle(Shape):
    """Class Circle: inherits from Shape and include method area"""
    pi = 3.14159

    def __init__(self, r=1, x=0, y=0):
        Shape.__init__(self, x, y)
        self.radius = r

    def area(self):
        """method area class Circle: return area of a circle"""
        return self.radius * self.radius * self.pi

    def __str__(self):
        return "Circle of radius %s at coordinates (%d, %d)" \
               % (self.radius, self.x, self.y)
