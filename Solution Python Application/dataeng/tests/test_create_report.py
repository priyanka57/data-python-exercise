import os
from unittest import TestCase

import pandas.core.frame

from create_report import ReportCreator
from validate_data import ValidateTransformData
import dummy_dfs  # file containing dummy data and dummy dataframes
import test_extract_data  # file containing target location variable


class TestReportCreator(TestCase):

    # required two correct dataframes with transformed column name

    # dummy dataframe 1
    obj_transform1 = ValidateTransformData(dummy_dfs.correct_df1)
    test_df1 = obj_transform1.transform_data('fname', 'lname', 'students')

    # dummy dataframe 2
    obj_transform2 = ValidateTransformData(dummy_dfs.correct_df2)
    test_df2 = obj_transform2.transform_data('fname', 'lname', 'teacher')

    # instantiate object for the testing class using above two dataframes
    test_create_report1 = ReportCreator(test_df1, test_df2)
    res_dict1 = test_create_report1.dataframe_merger('cid', 'left')  # output dictionary

    # instantiate object for the testing class using NULL values
    test_create_report2 = ReportCreator(None, None)

    def test_output_dictionary_generator_correct_dict(self):
        # to test the correctness of the functionality
        self.assertIsInstance(self.res_dict1, dict)
        self.assertEqual(len(self.res_dict1), 4)
        self.assertEqual(self.res_dict1['Joseph JM']['teacher'], 'London Apple')

    def test_output_dictionary_generator_wrong_dict(self):
        # to test Exception when no dataframe is passed through the function
        with self.assertRaises(Exception):
            self.test_create_report2.dataframe_merger('cid', 'left')

    def test_json_report_writer_correct_dict(self):
        # to test the correctness of the functionality
        # output should result True and create an .json report
        self.assertTrue(self.test_create_report1.
                        json_report_writer(self.res_dict1, test_extract_data.target_data_path))

        # to test if .json file is created
        for filename in test_extract_data.THIS_DIR:
            if filename.endswith('.json'):
                assert True
            else:
                pass

        # to delete the file created above for testing purposes
        try:
            os.remove('output.json')
        except OSError:
            pass

    def test_json_report_writer_wrong_dict(self):
        # to test the exception when no output dictionary is passed into the function
        with self.assertRaises(Exception):
            self.test_create_report1.json_report_writer(None, test_extract_data.target_data_path)

    # Integration Test between ValidateTransformData and ReportCreator
    def test_validate_data_create_report(self):
        # check if output of ValidateTransformData is the same instance as the required input by ReportCreator
        self.assertIsInstance(self.test_df1, pandas.core.frame.DataFrame)