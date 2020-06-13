import pytest
from src.DataFrame import DataFrameClass
import os

@pytest.fixture(scope='function')
def dataframe():
    print('Doing setup for test...')
    data_frame = DataFrameClass(os.path.join(os.path.dirname(__file__), 'files/Alcohol.csv'))
    yield data_frame
    data_frame = None
    print('Test cleanup...')
