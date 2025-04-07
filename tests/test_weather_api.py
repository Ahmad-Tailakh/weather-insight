import unittest
from unittest.mock import patch
from src.weather_api import get_weather


class TestWeatherAPI(unittest.TestCase):

    def test_valid_city(self):
        # Simulate a valid city response
        with patch('src.weather_api.requests.get') as mock_get:
            mock_get.return_value.json.return_value = {
                'main': {'temp': 15},
                'weather': [{'description': 'clear sky'}],
                'name': 'Berlin',
                'cod': 200
            }
            result = get_weather("Berlin")
            self.assertIsNotNone(result)
            self.assertIn("Temperature (°C)", result)
            self.assertEqual(result['City'], "Berlin")
            self.assertEqual(result['Weather'], "clear sky")

    def test_invalid_city(self):
        # Simulate an invalid city response (e.g., 404 error)
        with patch('src.weather_api.requests.get') as mock_get:
            mock_get.return_value.json.return_value = {'message': 'city not found', 'cod': '404'}
            result = get_weather("ThisCityDoesNotExist")
            self.assertIsNone(result)


if __name__ == '__main__':
    unittest.main()
