from unittest.mock import Mock

from praktikum.burger import Burger
from praktikum.ingredient_types import INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_SAUCE


class TestBurger:

    def test_set_buns(self):
        burger = Burger()
        bun = Mock()

        # Установка булочки
        burger.set_buns(bun)

        # Проверка, что булочка установлена правильно
        assert burger.bun == bun

    def test_add_ingredient(self):
        burger = Burger()
        ingredient = Mock()

        # Добавление ингредиента
        burger.add_ingredient(ingredient)

        # Проверка, что ингредиент добавлен
        assert len(burger.ingredients) == 1 and burger.ingredients[0] == ingredient

    def test_remove_ingredient(self):
        burger = Burger()
        ingredient1 = Mock()
        ingredient2 = Mock()

        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)

        # Удаление первого ингредиента
        burger.remove_ingredient(0)

        # Проверка, что первый ингредиент удален
        assert len(burger.ingredients) == 1 and burger.ingredients[0] == ingredient2

    def test_move_ingredient(self):
        burger = Burger()
        ingredient1 = Mock()
        ingredient2 = Mock()
        ingredient3 = Mock()

        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)
        burger.add_ingredient(ingredient3)

        # Перемещение ингредиента
        burger.move_ingredient(0, 2)

        # Проверка порядка ингредиентов
        assert burger.ingredients == [ingredient2, ingredient3, ingredient1]

    def test_get_price(self):
        burger = Burger()
        bun = Mock()
        bun.get_price.return_value = 100
        burger.set_buns(bun)

        ingredient1 = Mock()
        ingredient1.get_price.return_value = 100

        ingredient2 = Mock()
        ingredient2.get_price.return_value = 100

        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)

        # Проверка вычисления цены
        assert burger.get_price() == 400

    def test_get_receipt(self):
        burger = Burger()
        bun = Mock()
        bun.get_name.return_value = "black bun"
        bun.get_price.return_value = 100

        ingredient1 = Mock()
        ingredient1.get_name.return_value = "cutlet"
        ingredient1.get_type.return_value = INGREDIENT_TYPE_FILLING
        ingredient1.get_price.return_value = 100

        ingredient2 = Mock()
        ingredient2.get_name.return_value = "hot sauce"
        ingredient2.get_type.return_value = INGREDIENT_TYPE_SAUCE
        ingredient2.get_price.return_value = 100

        burger.set_buns(bun)
        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)

        # Ожидаемый чек
        expected_receipt = (
            "(==== black bun ====)\n"
            "= filling cutlet =\n"
            "= sauce hot sauce =\n"
            "(==== black bun ====)\n\n"
            "Price: 400"
        )

        # Проверка генерации чека
        assert burger.get_receipt() == expected_receipt
