import Ingredient


class Recipe:
    def __init__(self, title, ingredients):
        self.title = title
        self._ingredients = list(ingredients)
    def add_ingredient(self, ingredient: Ingredient.Ingredient):
        t = 0
        for i in self._ingredients:
            if ingredient == i:
                i.quantity = ingredient.quantity + i.quantity
                t = 1
                break
        if t == 0:
            self._ingredients.append(ingredient)
    @staticmethod
    def is_valid_ratio(ratio):
        if isinstance(ratio, float) or isinstance(ratio, int):
            return ratio > 0
        else:
            return False
    def scale(self, ratio: float):
        new_ingredients = []
        for i in self._ingredients:
            new_ingredients.append(Ingredient.Ingredient(i.name, i.quantity * ratio, i.unit))
        return Recipe(self.title, new_ingredients)
    def __len__(self):
        return len(self._ingredients)
    def __str__(self):
        s = f"{self.title} RECIPE:\n"
        for i in self._ingredients:
            s += str(i) + "\n"
        return s

