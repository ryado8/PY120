class Animal:
    def __init__(self, color):
        self._color = color

    @property
    def color(self):
        return self._color


class Cat(Animal):
    pass


class Bird(Animal):
    pass


cat1 = Cat("Black")
print(cat1.color)

# MRO order
# Cat => Animal
