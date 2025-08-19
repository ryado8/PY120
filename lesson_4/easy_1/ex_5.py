class Fruit:
    def __init__(self, name):
        my_name = name

class Pizza:
    def __init__(self, name):
        self.my_name = name

# Pizza will create objects with an instance variable my_name while fruit objects will not have
# an instance variable since my_name is simply a local variable within the initializer.