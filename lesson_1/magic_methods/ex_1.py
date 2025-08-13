class Car:

    def __init__(self, model, year, color):
        self._model = model
        self._year = year
        self._color = color

    def __str__(self):
        return f"{self._color.capitalize()} {self._year} {self._model}"

    def __repr__(self):
        return f"Car({repr(self._model)}, {self._year}, {repr(self._color)})"

vwbuzz = Car('ID.Buzz', 2024, 'red')
print(vwbuzz)        # Red 2024 ID.Buzz
print(repr(vwbuzz))  # Car('ID.Buzz', 2024, 'red')