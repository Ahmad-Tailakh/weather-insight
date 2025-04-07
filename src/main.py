from src.weather_api import get_weather
from src.data_handler import save_to_csv
from src.logger import logger


# Function to fetch weather data for multiple cities
def fetch_weather_for_multiple_cities(cities):
    weather_data = []
    for city in cities:
        weather = get_weather(city)
        if weather:
            weather_data.append(weather)
        else:
            logger.error(f"Failed to get weather for {city}")

    # Save the collected data to a CSV file
    save_to_csv(weather_data, "../weather_data.csv")


if __name__ == "__main__":
    # Direct call for manual execution if needed
    cities = ["Berlin", "London", "New York"]  # Add more cities as needed
    fetch_weather_for_multiple_cities(cities)
