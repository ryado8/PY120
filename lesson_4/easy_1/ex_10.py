class Cat:
    _cats_count = 0

    def __init__(self, type):
        self.type = type
        self.__class__._cats_count += 1

    @classmethod
    def cats_count(cls):
        return cls._cats_count

"""
The _cats_count is a class variable that counts how many cat objects have been instantiated by the class.
The initializer increments the _cats_count variable by 1 every time a new object is instantiated.
"""

cat1 = Cat('luffy')
cat2 = Cat('pom')
cat3 = Cat('new')

print(Cat.cats_count())