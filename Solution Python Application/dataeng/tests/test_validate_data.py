from unittest import TestCase
import numpy as np
from validate_data import ValidateTransformData
import dummy_dfs  # file containing dummy data and dummy dataframes


class TestValidateTransformData(TestCase):
    # different objects to instantiate different dataframes generated through the input data
    test_validate_data1 = ValidateTransformData(dummy_dfs.df_pk_null)  # to test primary key
    test_validate_data2 = ValidateTransformData(dummy_dfs.df_empty)  # to test empty
    test_validate_data3 = ValidateTransformData(dummy_dfs.correct_df1)  # to test correctness
    test_validate_data4 = ValidateTransformData(dummy_dfs.df_null)  # to test null values

    def test_check_if_valid_data_redundant_pk(self):
        # to test primary check validation
        with self.assertRaises(Exception):
            self.test_validate_data1.check_if_valid_data('id')

    def test_check_if_valid_data_null_value(self):
        # to check null value validation
        with self.assertRaises(Exception):
            self.test_validate_data4.check_if_valid_data('id')

    def test_check_if_valid_data_empty(self):
        # to check empty dataframe validation
        with self.assertRaises(Exception):
            self.test_validate_data2.check_if_valid_data('id')

    def test_check_if_valid_true_data(self):
        # to check all of the validations passes with the right data
        self.assertTrue(self.test_validate_data3.check_if_valid_data('id'))

    def test_transform_data_right_df(self):
        # to check the correctness of the right input data
        check_df = ['Kia KA', 'Joseph JM', 'Krish PT', 'John XY']
        result = self.test_validate_data3.transform_data('fname', 'lname', 'students')
        self.assertEqual(result['students'].to_list(), check_df)

    def test_transform_data_wrong_df(self):
        # to check the error exception wihen combining different data formats.
        with self.assertRaises(np.core._exceptions._UFuncNoLoopError):
            self.test_validate_data1.transform_data('id', 'Name', 'Combined')
