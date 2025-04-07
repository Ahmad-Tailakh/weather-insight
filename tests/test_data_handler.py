# tests/test_data_handler.py
import unittest
import os
from src.data_handler import save_to_csv


class TestDataHandler(unittest.TestCase):

    def test_save_to_csv(self):
        """Test that the data is correctly saved to a CSV file."""
        data = [{"Temperature (°C)": 20, "City": "Berlin"}]
        filename = "test_weather_data.csv"

        save_to_csv(data, filename)

        # Check if the file was created
        self.assertTrue(os.path.exists(filename))

        # Clean up the file after test
        if os.path.exists(filename):
            os.remove(filename)


if __name__ == '__main__':
    unittest.main()
