import Recipe
from Ingredient import Ingredient


class ShoppingList:
    def __init__(self, _items=None):
        if _items is None:
            self._items = []
        else:
            self._items = list(_items)
    def add_recipe(self, recipe: Recipe.Recipe, portions: float ):
        if portions <= 0:
            raise ValueError('Количество порций должно быть положительным')
        new_recipe = recipe.scale(portions)
        for i in new_recipe._ingredients:
            self._items.append((i, recipe.title))
    def remove_recipe(self, title: str):
        new_items = []
        for i in self._items:
            if i[1] != title:
                new_items.append(i)
        self._items = new_items
    def get_list(self):
        d = {}
        for i in self._items:
            ingredient = i[0]
            key = (ingredient.name, ingredient.unit)
            if key in d:
                d[key] += ingredient.quantity
            else:
                d[key] = ingredient.quantity
        result = []
        for i in d:
            name, unit = i
            result.append(Ingredient(name, d[i], unit))
        result.sort(key=lambda x: x.name)
        return result
    def __add__(self, other):
        new_list = ShoppingList()
        new_list._items = list(self._items) + list(other._items)
        return new_list
