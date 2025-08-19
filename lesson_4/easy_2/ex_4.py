class Greeting:
    def greet(self, message):
        print(message)

class Hello(Greeting):
    def hi(self):
        self.greet('Hello')

class Goodbye(Greeting):
    def bye(self):
        self.greet('Goodbye')

hello = Hello()
hello.hi() # prints 'hello'

hello = Hello()
hello.bye() # AttributeError

hello = Hello()
hello.greet() # ArgumentError

hello = Hello()
hello.greet('Goodbye') # prints "Goodbye"

Hello.hi() # TypeError