import pytest
from Ingredient import Ingredient
from Recipe import Recipe
from ShoppingList import ShoppingList


def test_init():
    ingr = Ingredient("Мука", 10.0, "г")
    assert ingr.name == "Мука"
    assert ingr.quantity == 10.0
    assert ingr.unit == "г"
def test_str():
    ingr = Ingredient("Мука", 10.0, "г")
    assert str(ingr) == "Мука: 10.0 г"
def test_eq_same():
    ingr1 = Ingredient("Мука", 10.0, "г")
    ingr2 = Ingredient("Мука", 20.0, "г")
    assert ingr1 == ingr2
def test_eq_name_dif():
    ingr1 = Ingredient("Мука", 10.0, "г")
    ingr2 = Ingredient("Щука", 20.0, "г")
    assert ingr1 != ingr2
def test_eq_unit_dif():
    ingr1 = Ingredient("Мука", 10.0, "г")
    ingr2 = Ingredient("Мука", 20.0, "кг")
    assert ingr1 != ingr2
def test_recipe_init():
    ingr1 = Ingredient("Хлеб", 10.0, "г")
    ingr2 = Ingredient("колбаса", 20.0, "кг")
    recipe = Recipe("БУТЕРБРОД", [ingr1, ingr2])
    assert recipe.title == "БУТЕРБРОД"
    assert recipe._ingredients == [ingr1, ingr2]
def test_recipe_add():
    ingr1 = Ingredient("Хлеб", 10.0, "г")
    recipe = Recipe("buter", [ingr1])
    ingr2 = Ingredient("колбаса", 20.0, "кг")
    recipe.add_ingredient(ingr2)
    assert recipe._ingredients == [ingr1, ingr2]
def test_recipe_add_eq():
    ingr1 = Ingredient("Хлеб", 10.0, "г")
    ingr2 = Ingredient("Хлеб", 30.0, "г")
    recipe = Recipe("buter", [ingr1])
    recipe.add_ingredient(ingr2)
    assert len(recipe) == 1
    assert recipe._ingredients[0].quantity == 40.0
def test_recipe_scale_newRecipe():
    ingr1 = Ingredient("Хлеб", 10.0, "г")
    ingr2 = Ingredient("колбаса", 20.0, "кг")
    recipe = Recipe("buter", [ingr1, ingr2])
    new_recipe = recipe.scale(2)
    assert new_recipe is not recipe
def test_recipe_scale_multi():
    ingr1 = Ingredient("Хлеб", 10.0, "г")
    ingr2 = Ingredient("колбаса", 20.0, "кг")
    recipe = Recipe("buter", [ingr1, ingr2])
    new_recipe = recipe.scale(2)
    assert new_recipe._ingredients[0].quantity == 20.0
    assert new_recipe._ingredients[1].quantity == 40.0
def test_recipe_error():
    ingr1 = Ingredient("Хлеб", 10.0, "г")
    ingr2 = Ingredient("колбаса", 20.0, "кг")
    recipe = Recipe("buter", [ingr1, ingr2])
    with pytest.raises(ValueError):
        recipe.scale(0)
def test_ShoppingList_add():
    ingr1 = Ingredient("Хлеб", 10.0, "г")
    recipe = Recipe("buter", [ingr1])
    sl = ShoppingList()
    sl.add_recipe(recipe, 2)
    assert len(sl._items) == 1
    assert sl._items[0][0].quantity == 20.0
def test_ShoppingList_error():
    ingr1 = Ingredient("Хлеб", 10.0, "г")
    recipe = Recipe("buter", [ingr1])
    sl = ShoppingList()
    with pytest.raises(ValueError):
        sl.add_recipe(recipe, 0)
def test_ShoppingList_remove():
    ingr1 = Ingredient("Хлеб", 10.0, "г")
    recipe = Recipe("buter", [ingr1])
    recipe1 = Recipe('bulka', [Ingredient('Мука', 500, 'г')])
    sl = ShoppingList()
    sl.add_recipe(recipe, 1)
    sl.add_recipe(recipe1, 1)
    sl.remove_recipe("buter")
    assert len(sl._items) == 1
    assert sl._items[0][1] == "bulka"
def test_ShoppingList_remove_nothing():
    ingr1 = Ingredient("Хлеб", 10.0, "г")
    recipe = Recipe("buter", [ingr1])
    recipe1 = Recipe('bulka', [Ingredient('Мука', 500.0, 'г')])
    sl = ShoppingList()
    sl.add_recipe(recipe, 1)
    sl.add_recipe(recipe1, 1)
    sl.remove_recipe("krabsburger")
    assert len(sl._items) == 2
def test_ShoppingList_getList_eq():
    recipe = Recipe('bulka', [Ingredient('Мука', 500.0, 'г')])
    recipe1 = Recipe('buter', [Ingredient('Мука', 100.0, 'г')])
    sl = ShoppingList()
    sl.add_recipe(recipe, 1)
    sl.add_recipe(recipe1, 1)
    result = sl.get_list()
    assert len(result) == 1
    assert result[0].quantity == 600.0
def test_ShoppingList_getList_sort():
    recipe = Recipe('bulka', [Ingredient('Мука', 500.0, 'г'), Ingredient('Щука', 500.0, 'г')])
    sl = ShoppingList()
    sl.add_recipe(recipe, 1)
    result = sl.get_list()
    assert result[0].name == 'Мука'
    assert result[1].name == "Щука"
def test_ShoppingList_add_comb():
    recipe1 = Recipe('bulka', [Ingredient('Мука', 500.0, 'г'), Ingredient('Щука', 500.0, 'г')])
    recipe2= Recipe('сладкая булка', [Ingredient('Сахар', 500.0, 'г'), Ingredient('Клубника', 500.0, 'г')])
    sl1 = ShoppingList()
    sl2 = ShoppingList()
    sl1.add_recipe(recipe1, 1)
    sl2.add_recipe(recipe2, 1)
    sl3 = sl1  + sl2
    assert len(sl3._items) == 4
def test_add_0change():
    recipe1 = Recipe('bulka', [Ingredient('Мука', 500.0, 'г'), Ingredient('Щука', 500.0, 'г')])
    recipe2 = Recipe('сладкая булка', [Ingredient('Сахар', 500.0, 'г'), Ingredient('Клубника', 500.0, 'г')])
    sl1 = ShoppingList()
    sl2 = ShoppingList()
    sl1.add_recipe(recipe1, 1)
    sl2.add_recipe(recipe2, 1)
    sl3 = sl1 + sl2
    assert len(sl1._items) == 2
    assert len(sl2._items) == 2