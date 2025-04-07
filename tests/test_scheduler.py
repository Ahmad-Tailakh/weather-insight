import unittest
from unittest.mock import patch
import schedule
from src import scheduler

class TestScheduler(unittest.TestCase):

    @patch('src.scheduler.fetch_weather_for_multiple_cities')
    def test_job_is_scheduled(self, mock_fetch):
        # Clear any previous jobs
        schedule.clear()

        # Call the scheduling function
        scheduler.schedule_weather_fetching()

        # There should be exactly one job scheduled
        jobs = schedule.get_jobs()
        self.assertEqual(len(jobs), 1)

        # Run the scheduled job manually
        for job in jobs:
            job.job_func()

        # Verify that the mocked fetch_weather_for_multiple_cities was called
        mock_fetch.assert_called_once()

if __name__ == '__main__':
    unittest.main()
