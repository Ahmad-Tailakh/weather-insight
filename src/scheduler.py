import schedule
import time
from src.main import fetch_weather_for_multiple_cities

def job():
    cities = ["Berlin", "London", "New York"]
    fetch_weather_for_multiple_cities(cities)

def schedule_weather_fetching():
    # Schedule the job every day at 7:00 AM
    schedule.every().day.at("07:00").do(job)
    print("✅ Weather fetching scheduled to run daily at 07:00...")

def run_scheduler():
    while True:
        schedule.run_pending()
        time.sleep(60)

if __name__ == "__main__":
    schedule_weather_fetching()
    run_scheduler()
