from src.DataFrame import DataFrameClass as DataFrameClass

def test_data_frame_read():
    data_frame = DataFrameClass('http://vincentarelbundock.github.io/Rdatasets/csv/mosaicData/Alcohol.csv')
    assert data_frame is not None


def test_filter_column_on_regex():
    data_frame = DataFrameClass('http://vincentarelbundock.github.io/Rdatasets/csv/mosaicData/Alcohol.csv')
    assert len(data_frame.list_columns()) > len(data_frame.filter_out_columns_regex('[a]').list_columns())


def test_filter_column_on_value():
    data_frame = DataFrameClass('http://vincentarelbundock.github.io/Rdatasets/csv/mosaicData/Alcohol.csv')
    assert data_frame.filter_out_column_on_value('country','India').get_record_count() == 2


