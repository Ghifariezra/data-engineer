import pandas as pd

def extract_func(**kwargs):
    dfs = pd.read_csv(kwargs.get('url_git'))

    return dfs