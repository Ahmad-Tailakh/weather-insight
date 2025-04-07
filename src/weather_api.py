import requests
from config import API_KEY, BASE_URL, DEFAULT_UNITS
from .logger import logger

def get_weather(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": DEFAULT_UNITS
    }
    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()
        data = response.json()
        logger.info(f"Fetched weather data for {city}")
        return {
            "City": data["name"],
            "Temperature (°C)": data["main"]["temp"],
            "Weather": data["weather"][0]["description"]
        }
    except requests.exceptions.HTTPError as http_err:
        logger.error(f"HTTP error for {city}: {http_err}")
    except Exception as err:
        logger.error(f"General error for {city}: {err}")
    return None
