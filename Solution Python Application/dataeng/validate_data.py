"""
Class containing methods to do the
transformation/validation of ETL process,
It will check the input dataframes for
empty data, null values, primary key.
Method will transform the data column based on required output.
"""
import pandas as pd


class ValidateTransformData:
    """
    A class to validate and transform the data before
    it gets processed to create the desired report
    """

    def __init__(self, dataframe: pd.DataFrame):
        self.dataframe = dataframe

    def check_if_valid_data(self, primary_key: str) -> bool:
        """
        method to validate dataframes coming from input file
        :param primary_key: intakes file's primary key
        :return: boolean
        """
        # Check if dataframe is empty
        if self.dataframe.empty:
            raise Exception("Required data records empty. Finishing execution")

        # Primary Key Check
        if self.dataframe[primary_key].is_unique:
            pass
        else:
            raise Exception("Primary Key check is violated")

        # Check for nulls
        if self.dataframe.isnull().values.any():
            raise Exception("Null values found")

        return True

    def transform_data(self, column1: str
                       , column2: str, output_column: str) -> pd.DataFrame:
        """
        Transform validated data according to the business rules.
        first_name and last_name combining
        to form a string of 'first_name last_name'
        :param column1: referring to 'fname' column
        :param column2: referring to 'lname' column
        :param output_column: outputs a new column with combined name
        :return: dataframe with transformed column
        """
        # Combine 'first' and 'last' name columns to create a 'full' name column
        self.dataframe[output_column] = self.dataframe[column1] + ' ' + self.dataframe[column2]
        return self.dataframe
