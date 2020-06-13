from src.DataFrame import DataFrameClass as DataFrameClass

def test_data_frame_read(dataframe):
    assert dataframe is not None


def test_filter_column_on_regex(dataframe):
    assert len(dataframe.list_columns()) > len(dataframe.filter_out_columns_regex('[a]').list_columns())


def test_filter_column_on_value(dataframe):
    assert dataframe.filter_out_column_on_value('country', 'India').get_record_count() == 2
