class Cat:
    def __init__(self, name):
        self._name = name

    def greet(self):
        print(f"Hello! My name is {self.name}!")

    @property
    def name(self):
        return self._name

kitty = Cat('Sophie')
kitty.greet()