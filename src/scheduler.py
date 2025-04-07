import schedule
import time
from src.main import fetch_weather_for_multiple_cities


# Function to schedule the fetching of weather data
def schedule_weather_fetching():
    cities = ["Berlin", "London", "New York"]  # Add more cities as needed

    # Define the job to run every day at 7:00 AM
    schedule.every().day.at("07:00").do(fetch_weather_for_multiple_cities, cities)

    print("Weather fetching scheduled...")

    # Run the scheduled tasks
    while True:
        schedule.run_pending()
        time.sleep(60)  # Wait for a minute before checking again


# Run the schedule function
if __name__ == "__main__":
    schedule_weather_fetching()
