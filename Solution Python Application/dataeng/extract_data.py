"""
Takes two different input files and extracts meaningful data from them.
While data extraction, it will validate and transform data
"""
import pandas as pd
import pyarrow.parquet as pq
from validate_data import ValidateTransformData


class DataExtractor:
    """
    A class to bind different reading methods for each type of file extensions
    to extract the required data as dataframes.
    """

    def __init__(self, csv_file: str, parquet_file: str,
                 columns_to_read: list):
        self.csv_file = csv_file
        self.parquet_file = parquet_file
        self.columns_to_read = columns_to_read
        self.primary_key = self.columns_to_read[0]

    def csv_reader(self, csv_transformed_column_name) -> pd.DataFrame:
        """
        call this method to return a dataframe from .csv file
        :param csv_transformed_column_name: new name for transformed csv column
        :return: csv dataframe
        """
        # Check if csv file exists, then create the dataframe
        # using separator. Extract required columns
        # else throw an exception
        if self.csv_file.endswith('.csv'):
            csv_df = pd.read_csv(self.csv_file, sep='_', usecols=self.columns_to_read)
        else:
            raise FileNotFoundError("No CSV file found, check location.")

        # Extracted data needs to be validated through a method
        # from ValidateTransformData class
        csv_validate = ValidateTransformData(csv_df)
        if csv_validate.check_if_valid_data(self.primary_key):
            print("CSV Data valid, proceed to transform stage.")

        # If validated, a few columns will also get transformed
        # based on the required output
        csv_validate.transform_data(self.columns_to_read[1], self.columns_to_read[2],
                                    csv_transformed_column_name)
        print("Required CSV transformation completed.")
        return csv_df

    def parquet_reader(self, parquet_transformed_column_name) -> pd.DataFrame:
        """
        call this method to return a dataframe from .parquet file
        :param parquet_transformed_column_name: new name for the transformed column
        :return: parquet dataframe
        """
        # Check if parquet file exists, then create the dataframe
        # using separator.Extract required columns
        # else throw an exception
        if self.parquet_file.endswith('.parquet'):
            parquet_df = pq.read_table(self.parquet_file, columns=self.columns_to_read).to_pandas()
        else:
            raise FileNotFoundError("No Parquet file found, check location.")

        # Extracted data needs to be validated through
        # a method from ValidateTransformData class
        parquet_validate = ValidateTransformData(parquet_df)
        if parquet_validate.check_if_valid_data(self.primary_key):
            print("Parquet Data valid, proceed to transform stage.")

        # If validated, a few columns will also get transformed based on the required output
        parquet_validate.transform_data(self.columns_to_read[1], self.columns_to_read[2],
                                        parquet_transformed_column_name)
        print("Required Parquet transformation completed.")
        return parquet_df
