"""
Main entry point of the python application
The application will take two input files with csv and parquet extensions.
Based on the matched data based on the same class ID,
it will create the required json report in the format
{student:{class ID, teacher}}
Author: Priyanka Goyal
"""
import sys
from create_report import ReportCreator
from extract_data import DataExtractor

# To run python application from the command line,
# Pass input/output file names as arguments
CSV_FILENAME = sys.argv[1]
PARQUET_FILENAME = sys.argv[2]
OUTPUT_LOCATION = sys.argv[3]

# To run script from IDE, change locations for input/output files
# and remove the commented next three lines
# CSV_FILENAME = '<directory path where csv file is stored>/students.csv'
# PARQUET_FILENAME = '<directory path where parquet file is stored>/teachers.parquet'
# OUTPUT_LOCATION = '<directory path where output must be stored>/final_report.json'

# Example
# CSV_FILENAME = '/home/priya/Desktop/data_python_exercise/data_engineer/students.csv'
# PARQUET_FILENAME = '/home/priya/Desktop/data_python_exercise/data_engineer/teachers.parquet'
# OUTPUT_LOCATION = '/home/priya/Desktop/final_report.json'

# VARIABLES

# To read columns from input files.
# Here both files have same column structure hence unified the list
# First column should be the primary key.
INPUT_FILES_COLUMNS = ['id', 'fname', 'lname', 'cid']

# New Column name for Students
CSV_NEW_COLUMN = 'students'

# New Column name for Teacher
PARQUET_NEW_COLUMN = 'teacher'

# Key on which two data frames are merged
KEY = 'cid'

# Type of merge
HOW = 'left'

if __name__ == '__main__':
    # instantiate DataExtractor and use the two read methods
    # to create csv and parquet input dataframes.
    input_data = DataExtractor(CSV_FILENAME, PARQUET_FILENAME, INPUT_FILES_COLUMNS)
    csv_input_df = input_data.csv_reader(CSV_NEW_COLUMN)
    parquet_input_df = input_data.parquet_reader(PARQUET_NEW_COLUMN)

    # instantiate ReportCreator class and use the two methods
    # to generate output dictionary and create the output json report
    output_data = ReportCreator(csv_input_df, parquet_input_df)
    json_output_dict = output_data.dataframe_merger(KEY, HOW)
    output_data.json_report_writer(json_output_dict, OUTPUT_LOCATION)
