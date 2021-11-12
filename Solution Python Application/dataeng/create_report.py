"""
Takes two dataframes as an input and provides method(s)
to create a multi level dictionary containing student names
with their class ID and teacher name.
Once the output dictionary is ready, the output is written to
a json file.
"""
import json
import pandas as pd


class ReportCreator:
    """
    A class to take two dataframes as an input
    and merge them based on the common key and orientation.
    A multi level dictionary is created based on the merged dataframes
    and the output is written to generate a json report.
    """

    def __init__(self, df1: pd.DataFrame, df2: pd.DataFrame):
        self.df1 = df1
        self.df2 = df2

    def dataframe_merger(self, common_key: str,
                         orientation: str) -> dict:
        """
        this method will take two dataframes and output a
        hierarchy dictionary
        :param orientation: how two columns should be merged
        :param common_key: on this column key
        :return: output data dictionary
        """
        # If both dataframe exists then proceed else throw an exception
        if not self.df1.empty and not self.df2.empty:
            # merge csv with parquet on left side on cid common column (SQL Left join)
            output_table = self.df1.merge(self.df2, on=common_key, how=orientation)

            # initialize dictionary to store data in multi levels
            json_dict = {}
            for row in output_table.iterrows():
                # row[0] is column name, start with the data
                row_data = row[1]
                # create dictionary with student as a key and values
                # as a dictionary containing information on
                # class ID and teacher name
                json_dict[row_data.students] = {"class ID": row_data.cid,
                                                "teacher": row_data.teacher}
        else:
            raise Exception("Dataframe(s) not found.")

        return json_dict

    @staticmethod
    def json_report_writer(output_dict: dict,
                           target: str) -> bool:
        """
        if dictionary exists, write it to generate a json output file
         to desired location else throw an exception
        :param output_dict: dictionary containing output contents
        :param target: desired location of output file
        :return: True if succeeds
        """
        if output_dict:
            with open(target, 'w') as json_file:
                json.dump(output_dict, json_file)
            print("Output report ready.")
        else:
            raise Exception("Couldn't write output contents to JSON report.")
        return True
