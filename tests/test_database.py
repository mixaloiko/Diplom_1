import pytest

from praktikum.database import Database


class TestDatabase:

    def test_available_buns(self):
        # Создаем экземпляр Database
        db = Database()

        # Получаем список доступных булочек
        buns = db.available_buns()

        # Проверяем количество булочек, названия и цены булочек
        assert (len(buns) == 3
                and buns[0].get_name() == "black bun"
                and buns[0].get_price() == 100
                and buns[1].get_name() == "white bun"
                and buns[1].get_price() == 200
                and buns[2].get_name() == "red bun"
                and buns[2].get_price() == 300)

    @pytest.mark.parametrize("index, expected_name, expected_price", [
        (0, "hot sauce", 100),
        (1, "sour cream", 200),
        (2, "chili sauce", 300),
        (3, "cutlet", 100),
        (4, "dinosaur", 200),
        (5, "sausage", 300)
    ])
    def test_available_ingredients(self, index, expected_name, expected_price):
        # Создаем экземпляр Database
        db = Database()

        # Получаем список доступных ингредиентов
        ingredients = db.available_ingredients()

        # Проверяем количество ингредиентов, названия и цены ингредиентов
        assert (len(ingredients) == 6
                and ingredients[index].get_name() == expected_name
                and ingredients[index].get_price() == expected_price)

