"""Modul circle: include class Circle. """
class Circle:
    all_circle = []  # class variable contains a list of all instances of the class created
    pi = 3.12159
    def __init__(self, r=1):
        """Create an example Circle with the specified values radius"""
        self.radius = r
        self.__class__.all_circle.append(self)
    def area(self):
        """calculating the area of a circle for a Circle instance"""
        return self.__class__.pi * self.radius * self.radius

    @staticmethod
    def total_area():
        """static method for calculating the area of all Circle"""
        total = 0
        for c in Circle.all_circle:
            total = total + c.area()
        return total
