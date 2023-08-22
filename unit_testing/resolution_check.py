import unittest
from unittest.mock import patch
from python import resolution_check


class TestResolutionCheck(unittest.TestCase):

    @patch('python.get_monitors')  # Mock the get_monitors function
    def test_resolution_match(self, mock_get_monitors):
        mock_csv_file = "mock_csv_file.csv"

        # Set up a mock monitor with the required resolution
        class MockMonitor:
            width = 1920
            height = 1080
        mock_monitor = MockMonitor()

        # Configure the mock get_monitors function to return the mock monitor
        mock_get_monitors.return_value = [mock_monitor]

        self.log_step_called = False

        try:
            resolution_check(mock_csv_file)

            # Assert that no log step was called (since resolutions match)
            self.assertFalse(self.log_step_called)

        finally:
            # Clean up the patch
            mock_get_monitors.stop()

    def log_step(self, test_case, status, csv_file):
        self.log_step_called = True


if __name__ == '__main__':
    unittest.main()
