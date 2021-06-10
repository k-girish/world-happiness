import pandas as pd
from IPython.core.display import display


def view_all_df(temp):
    """
    This utility function can be used to view all columns and rows of a pandas dataframe
    :param temp: the pandas dataframe to view
    """
    with pd.option_context('display.max_rows', None, 'display.max_columns', None, 'display.max_colwidth', -1):
        display(temp)
