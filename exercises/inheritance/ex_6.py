class TowingMixin:
    def tow(self):
        print("I can tow a trailer!")


class Truck(TowingMixin):
    pass


class Car:
    pass


# Comments show expected output
truck1 = Truck()
truck1.tow()  # I can tow a trailer!

car1 = Car()
car1.tow()
# AttributeError: 'Car' object has no attribute 'tow'
