import unittest
from unittest.mock import patch
from python import cuda_check


class TestCudaCheck(unittest.TestCase):

    # Mock the torch.cuda.is_available function
    @patch('python.torch.cuda.is_available')
    def test_cuda_available(self, mock_is_available):
        mock_csv_file = "mock_csv_file.csv"

        mock_is_available.return_value = True

        self.log_step_called = False

        def mock_log_step(test_case, status, csv_file):
            self.log_step_called = True

        # Mock the log_step function
        with patch('python.log_step', mock_log_step):
            try:
                cuda_check(mock_csv_file)

                # Assert that no log step was called (since CUDA is available)
                self.assertFalse(self.log_step_called)

            finally:
                # Clean up the patch
                mock_is_available.stop()

    # Mock the torch.cuda.is_available function
    @patch('python.torch.cuda.is_available')
    def test_cuda_unavailable(self, mock_is_available):
        mock_csv_file = "mock_csv_file.csv"

        mock_is_available.return_value = False

        self.log_step_called = False

        def mock_log_step(test_case, status, csv_file):
            self.log_step_called = True

        # Mock the log_step function
        with patch('python.log_step', mock_log_step):
            try:
                cuda_check(mock_csv_file)

                # Assert that log step was called (since CUDA is not available)
                self.assertTrue(self.log_step_called)

            finally:
                # Clean up the patch
                mock_is_available.stop()

    def log_step(self, test_case, status, csv_file):
        self.log_step_called = True


if __name__ == '__main__':
    unittest.main()
