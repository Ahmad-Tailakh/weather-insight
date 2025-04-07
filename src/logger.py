import logging
from logging.handlers import RotatingFileHandler

# Set up the logger with rotation
logger = logging.getLogger("WeatherAPI")
logger.setLevel(logging.DEBUG)

# Create a rotating file handler to keep the last 5 logs, each 1 MB
handler = RotatingFileHandler("weather_api.log", maxBytes=5 * 1024 * 1024, backupCount=5)
handler.setLevel(logging.DEBUG)

# Set the log format
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

# Add the handler to the logger
logger.addHandler(handler)
