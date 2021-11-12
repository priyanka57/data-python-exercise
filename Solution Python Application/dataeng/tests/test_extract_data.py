import os
from unittest import TestCase
import pandas as pd
from extract_data import DataExtractor

# variables to find the path of input/output files from where the current script is running
THIS_DIR = os.path.dirname(os.path.abspath(__file__))
csv_data_path = os.path.join(THIS_DIR, 'dummy_csv.csv')  # dummy input file
parq_data_path = os.path.join(THIS_DIR, 'parq_dummy.parquet')  # dummy input file
target_data_path = os.path.join(THIS_DIR, 'output.json')  # dummy output file

# variables for testing the dataframes
columns = ['id', 'fname', 'lname', 'cid']
trans_csv = 'students'
trans_parq = 'teacher'


class TestDataExtractor(TestCase):
    # different objects instantiated to avoid confusion and
    # test the functionality based on the testcase
    test_extract_data1 = DataExtractor(' ', parq_data_path, columns)  # no csv file
    test_extract_data2 = DataExtractor(csv_data_path, ' ', columns)  # no parquet file
    test_extract_data3 = DataExtractor('/tmp/test.txt', parq_data_path, columns)  # wrong csv file
    test_extract_data4 = DataExtractor(csv_data_path, '/tmp/test.txt', columns)  # wrong parquet file
    test_extract_data5 = DataExtractor(csv_data_path, parq_data_path, columns)  # correct data

    def test_csv_reader_no_file(self):
        # csv input parameter empty
        with self.assertRaises(FileNotFoundError):
            self.test_extract_data1.csv_reader(trans_csv)

    def test_parquet_reader_no_file(self):
        # parquet input parameter empty
        with self.assertRaises(FileNotFoundError):
            self.test_extract_data2.parquet_reader(trans_parq)

    def test_csv_reader_wrong_file(self):
        # wrong csv filetype
        with self.assertRaises(FileNotFoundError):
            self.test_extract_data3.csv_reader(trans_csv)

    def test_parquet_reader_wrong_file(self):
        # wrong parquet filetype
        with self.assertRaises(FileNotFoundError):
            self.test_extract_data4.parquet_reader(trans_parq)

    def test_csv_reader_dummy_file(self):
        # to check if functionality is creating dataframe from .csv file
        self.assertIsInstance(self.test_extract_data5.csv_reader(trans_csv), pd.DataFrame)

    def test_parquet_reader_dummy_file(self):
        # to check if functionality is creating dataframe from .parquet file
        self.assertIsInstance(self.test_extract_data5.parquet_reader(trans_parq), pd.DataFrame)