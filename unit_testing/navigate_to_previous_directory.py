import unittest
from unittest.mock import patch
from python import navigate_to_previous_directory


class TestNavigateToPreviousDirectory(unittest.TestCase):

    @patch('os.getcwd')  # Mock the os.getcwd function
    @patch('os.chdir')    # Mock the os.chdir function
    def test_navigate_to_previous_directory(self, mock_chdir, mock_getcwd):
        mock_getcwd.return_value = '/home/emumba/Desktop/Test_folder'

        navigate_to_previous_directory()

        mock_chdir.assert_called_once_with('/home/emumba/Desktop')


if __name__ == '__main__':
    unittest.main()
