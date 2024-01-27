class Rectangle:
    def __init__(self, l, b):
        self.l = l
        self.b = b

    def area(self):
        area = self.l * self.b
        print("Area of rectangle:", area)
        return area

    def perimeter(self):
        per = 2 * (self.l + self.b)
        print("Perimeter of rectangle:", per)
        return per


rl = Rectangle(7, 8)


rectangle_area = rl.area()
rectangle_perimeter = rl.perimeter()