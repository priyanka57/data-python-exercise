import os
from unittest import TestCase
import main


class MainTest(TestCase):

    # Find the path from where the project_integration_test.py file is running
    THIS_DIR = os.path.dirname(os.path.abspath(__file__))

    # join the parent directory (as we do not want to include /test dir in the path
    # with the main.py file name
    main_file_path = os.path.join(os.path.dirname(THIS_DIR), 'main.py')
    python_interpreter = 'python3.6'

    # generate command by taking the input output variables from main file
    command = python_interpreter + ' ' + main_file_path + ' ' + \
              main.CSV_FILENAME + ' ' + \
              main.PARQUET_FILENAME + ' ' + main.OUTPUT_LOCATION

    def test_main(self):
        # to check if the application fails at the system level
        result = os.system(self.command)
        self.assertEqual(result, 0)
