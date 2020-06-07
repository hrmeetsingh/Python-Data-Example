import pandas as pd
import numpy as np


class DataFrameClass:
    main_data_frame = None

    def __init__(self, source_csv_path=''):
        self.main_data_frame = pd.read_csv(source_csv_path)

    def print_table(self):
        print(self.main_data_frame)

    def filter_out_columns_regex(self, regex):
        self.main_data_frame = self.main_data_frame.filter(regex=regex)
        return self

    def list_columns(self):
        return self.main_data_frame.columns.to_list()

    def get_record_count(self):
        return len(self.main_data_frame.index)

    def filter_out_column_on_value(self, column, value):
        self.main_data_frame = self.main_data_frame.loc[np.where(self.main_data_frame[column] == value)]
        return self


if __name__ == '__main__':
    data_frame = DataFrameClass('http://vincentarelbundock.github.io/Rdatasets/csv/mosaicData/Alcohol.csv')
    print(data_frame.get_record_count())