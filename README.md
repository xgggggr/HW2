## система для управления рецептами
Описание: Это консольное приложение, которое позволяет создавать блюда, 
добавлять их в "рецепты", масштабировать порции и генерировать список покупок
Проект состоит из:
1) `Ingredient` - отдельный ингредиент (название, количество, единица измерения);
2) `Recipe` - рецепт блюда с набором ингредиентов;
3) `DietaryRecipe` - рецепт с диетической категорией;
4) `ShoppingList` — список покупок, суммирующий ингредиенты из нескольких рецептов.

УСТАНОВКА:
```
git clone https://github.com/xgggggr/HW2 
cd HW2
pip install -r requirements.txt
```

ИСПОЛЬЗОВАНИЕ:
```python
from Ingredient import Ingredient
from Recipe import Recipe
from DietaryRecipe import DietaryRecipe
from ShoppingList import ShoppingList

buter = Recipe("БУтер", [Ingredient("Хлеб", 20.0, "г")])
buter.add_ingredient(Ingredient("Сыр", 20.0, "г"))

sl = ShoppingList()
sl.add_recipe(buter, portions=2)
print(sl.get_list())
```
ЗАПУСК ТЕСТОВ:
```
pytest
```

## Автор
Тлеуж Айтеч Адамович, ББИ2504

