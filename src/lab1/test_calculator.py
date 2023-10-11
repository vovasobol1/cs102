import unittest
from calculator import calculator  # Импортируем функцию calculator

class TestCalculator(unittest.TestCase):

    def test_addition(self):
        # Проверяем, что калькулятор правильно складывает два числа
        result = calculator("2 + 3")
        self.assertEqual(result, "5")

    def test_subtraction(self):
        # Проверяем, что калькулятор правильно вычитает два числа
        result = calculator("5 - 2")
        self.assertEqual(result, "3")

    def test_multiplication(self):
        # Проверяем, что калькулятор правильно умножает два числа
        result = calculator("4 * 6")
        self.assertEqual(result, "24")

    def test_division(self):
        # Проверяем, что калькулятор правильно делит два числа
        result = calculator("8 / 4")
        self.assertEqual(result, "2.0")

    def test_invalid_input(self):
        # Проверяем, как калькулятор обрабатывает некорректный тип данных (сложение числа и строки)
        result = calculator("2 + 'abc'")
        self.assertEqual(result, "Введены неправильные значения!")

    def test_zero_division(self):
        # Проверяем, как калькулятор обрабатывает попытку деления на ноль
        result = calculator("5 / 0")
        self.assertEqual(result, "нельзя делить на ноль")

if __name__ == '__main__':
    unittest.main()
