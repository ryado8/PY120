class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def area(self):
        return self.width * self.height


rect = Rectangle(4, 5)

print(rect.width == 4)  # True
print(rect.height == 5)  # True
print(rect.area == 20)  # True
