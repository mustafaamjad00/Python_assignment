import unittest
import os
import tempfile
from python import compare_and_update_golden_log


class TestCompareAndUpdateGoldenLog(unittest.TestCase):

    def test_compare_and_update_golden_log(self):
        # Create temporary log and golden files
        with tempfile.NamedTemporaryFile(delete=False) as log_file:
            log_file.write(b"log contents")
        with tempfile.NamedTemporaryFile(delete=False) as golden_file:
            # Initialize golden contents to match log contents
            golden_file.write(b"log contents")

        # Call the function with the temporary file paths
        compare_and_update_golden_log(
            log_file.name, os.path.dirname(golden_file.name))

        # Read the updated golden file
        updated_golden_contents = ""
        with open(golden_file.name, 'r') as updated_golden:
            updated_golden_contents = updated_golden.read()

        # Assert that the contents of the golden file have been updated
        self.assertEqual(updated_golden_contents, "log contents")

        # Clean up the temporary files
        os.remove(log_file.name)
        os.remove(golden_file.name)


if __name__ == '__main__':
    unittest.main()
