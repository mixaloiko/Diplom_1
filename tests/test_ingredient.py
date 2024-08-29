from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE


class TestIngredient:

    def test_get_price(self):
        # Создаем ингредиент с определенной ценой
        ingredient = Ingredient(ingredient_type=INGREDIENT_TYPE_SAUCE, name='hot sauce', price=100)

        # Проверяем, что метод get_price возвращает корректную цену
        assert ingredient.get_price() == 100

    def test_get_name(self):
        # Создаем ингредиент с определенным названием
        ingredient = Ingredient(ingredient_type=INGREDIENT_TYPE_SAUCE, name='hot sauce', price=100)

        # Проверяем, что метод get_name возвращает корректное название
        assert ingredient.get_name() == 'hot sauce'

    def test_get_type(self):
        # Создаем ингредиент с определенным типом
        ingredient = Ingredient(ingredient_type=INGREDIENT_TYPE_SAUCE, name='hot sauce', price=100)

        # Проверяем, что метод get_type возвращает корректный тип
        assert ingredient.get_type() == INGREDIENT_TYPE_SAUCE
