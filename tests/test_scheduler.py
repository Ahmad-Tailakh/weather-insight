# tests/test_scheduler.py
import unittest
from unittest.mock import patch
from apscheduler.schedulers.background import BackgroundScheduler
from src.scheduler import scheduler

class TestScheduler(unittest.TestCase):

    @patch.object(BackgroundScheduler, 'start')  # Mock the start method
    def test_scheduler_start(self, mock_start):
        """Test if the scheduler is starting without errors."""
        scheduler.start()
        mock_start.assert_called_once()

if __name__ == '__main__':
    unittest.main()
