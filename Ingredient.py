
class Ingredient:
    def __init__(self, name, quantity, unit):
        self._name = name
        self.quantity = quantity
        self._unit = unit
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
        return f"{self._name}: {self._quantity} {self._unit}"
    def __repr__(self):
        return f"Ingredient('{self._name}', {self._quantity}, '{self._unit}')"
    def __eq__(self, other):
        if isinstance(other, Ingredient):
            return self._name == other._name and self._unit == other._unit
        else:
            return False