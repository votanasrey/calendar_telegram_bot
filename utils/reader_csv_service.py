import pandas as pd 

def call_read_csv(dir_filename):
    data = pd.read_csv(dir_filename)
    return data