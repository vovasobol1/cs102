import unittest
from unittest.mock import patch
from main import getWeather
from config import weatherApiToken

class TestGetWeather(unittest.TestCase):
    # Этот класс представляет набор юнит-тестов для функции getWeather.

    @patch('requests.get')
    def test_get_weather_exception(self, mock_get):
        # Этот метод тестирует обработку исключения в функции getWeather при неудачном запросе к апи

        # Мокируем запрос, чтобы изолировать функцию от фактического HTTP-запроса
        # mock_get - объект-замена для requests.get, который будет имитировать его вызов
        mock_get.side_effect = Exception("Test exception")

        # Вызываем функцию getWeather с неверным названием города
        result = getWeather('invalidcity', weatherApiToken)

        # Ожидаемый результат: строка с сообщением об ошибке.
        expected_result = 'Не удалось получить информацию о погоде. Пожалуйста, проверьте название города.'

        # Сравниваем фактический результат с ожидаемым, чтобы убедиться, что функция правильно обрабатывает ошибку.
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()



