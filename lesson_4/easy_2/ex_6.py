class Cat:
    def __init__(self, type):
        self.type = type

    def __str__(self):
        return f"I am a {self.type}"

print(Cat('hairball'))
# <__main__.Cat object at 0x10695eb10>