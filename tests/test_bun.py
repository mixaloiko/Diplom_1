from praktikum.bun import Bun


class TestBun:

    def test_get_name(self):
        # Создаем объект Bun с определенным именем и ценой
        bun = Bun(name='black bun', price=100)

        # Проверяем, что метод get_name возвращает корректное имя
        assert bun.get_name() == 'black bun'

    def test_get_price(self):
        # Создаем объект Bun с определенным именем и ценой
        bun = Bun(name='black bun', price=100)

        # Проверяем, что метод get_price возвращает корректную цену
        assert bun.get_price() == 100

