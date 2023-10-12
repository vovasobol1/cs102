import unittest
from unittest.mock import patch
from main import getWeather
from config import weatherApiToken

class TestGetWeather(unittest.TestCase):

    @patch('requests.get')
    def test_get_weather_successful(self, mock_get):
        # Мокируем запрос и настраиваем его ответ
        mock_response = mock_get.return_value
        mock_response.json.return_value = {
            'name': 'City',
            'main': {'temp': 20, 'humidity': 50},
            'wind': {'speed': 5},
            'sys': {'sunrise': 1634000000, 'sunset': 1634040000}
        }

        result = getWeather('City', weatherApiToken)
        expected_result = (
            "погода в City \n"
            "температура воздуха : 20°\n"
            "влажность :50% \n"
            "скорость ветра : 5м/с \n"
            "давление :1013мм \n"  
            "рассвет: 03:46:40 \n"
            "закат: 18:33:20 \n"
        )
        self.assertEqual(result, expected_result)

    @patch('requests.get')
    def test_get_weather_exception(self, mock_get):
        # Мокируем запрос, но настраиваем его на выброс исключения
        mock_get.side_effect = Exception("Test exception")

        result = getWeather('InvalidCity', 'your_token')
        expected_result = 'Не удалось получить информацию о погоде. Пожалуйста, проверьте название города.'
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()
