
class Ingredient:
    def __init__(self, name, quantity, unit):
        self.name = name
        self.quantity = quantity
        self.unit = unit
    @property
    def quantity(self):
        return self._quantity
    @quantity.setter
    def quantity(self, value):
        if value > 0:
            self._quantity = float(value)
        else:
            raise ValueError('Количество должно быть положительным')
    def __str__(self):
        return f"{self.name}: {self._quantity} {self.unit}"
    def __repr__(self):
        return f"Ingredient('{self.name}', {self._quantity}, '{self.unit}')"
    def __eq__(self, other):
        if isinstance(other, Ingredient):
            return self.name == other.name and self.unit == other.unit
        else:
            return False