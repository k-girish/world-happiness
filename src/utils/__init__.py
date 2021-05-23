import pandas as pd
from IPython.core.display import display


def view_all_df(temp):
    with pd.option_context('display.max_rows', None, 'display.max_columns', None):
        display(temp)
