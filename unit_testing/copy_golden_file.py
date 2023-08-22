import unittest
import os
from unittest.mock import patch
from python import copy_golden_file


class TestCopyGoldenFile(unittest.TestCase):

    @patch('python.log_to_file')  # Mock log_to_file function
    @patch('python.shutil.copy')   # Mock shutil.copy function
    @patch('python.os.path.exists')  # Mock os.path.exists function
    def test_copy_golden_file(self, mock_exists, mock_copy, mock_log_to_file):
        Testname = "Test_folder"
        GoldenFileName = "Test_Name.Golden"
        GoldenFileSource = "/home/emumba/Desktop"

        mock_exists.return_value = True  # Simulate that the source file exists

        with patch('python.Testname', Testname):
            with patch('python.GoldenFileName', GoldenFileName):
                with patch('python.GoldenFileSource', GoldenFileSource):
                    copy_golden_file()

        destination_path = os.path.join(Testname, GoldenFileName)

        mock_exists.assert_called_once_with(
            os.path.join(GoldenFileSource, GoldenFileName))
        mock_copy.assert_called_once_with(
            os.path.join(GoldenFileSource, GoldenFileName), destination_path)

        # Verify that log_to_file was called with the correct message
        expected_log_calls = [
            unittest.mock.call(destination_path),
            unittest.mock.call(
                f"Golden file {GoldenFileName} copied successfully to {destination_path}")
        ]
        mock_log_to_file.assert_has_calls(expected_log_calls)
        self.assertEqual(mock_log_to_file.call_count, 2)


if __name__ == '__main__':
    unittest.main()
