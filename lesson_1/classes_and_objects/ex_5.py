class Person:

    def __init__(self, first_name, last_name):
        self._validate_and_set_name(first_name, last_name)

    @property
    def name(self):
        return f"{self._first_name.capitalize()} {self._last_name.capitalize()}"

    @name.setter
    def name(self, full_name):
        first_name, last_name = full_name
        self._validate_and_set_name(first_name, last_name)

    def _validate_and_set_name(self, first, last):
        if not first.isalpha() or not last.isalpha():
            raise ValueError("Name must be alphabetic.")

        self._first_name = first
        self._last_name = last


actor = Person('Mark', 'Sinclair')
print(actor.name)              # Mark Sinclair
actor.name = ('Vin', 'Diesel')
print(actor.name)              # Vin Diesel
actor.name = ('', 'Diesel')
# ValueError: Name must be alphabetic.

character = Person('annIE', 'HAll')
print(character.name)          # Annie Hall
character = Person('Da5id', 'Meier')
# ValueError: Name must be alphabetic.

friend = Person('Lynn', 'Blake')
print(friend.name)             # Lynn Blake
friend.name = ('Lynn', 'Blake-John')
# ValueError: Name must be alphabetic.