import numpy as np
import pandas as pd
import warnings
warnings.filterwarnings('ignore')


def get_curriculum_log():
    colnames = ['date', 'endpoint', 'user_id', 'cohort_id', 'source_ip']
    df = pd.read_csv("PythonScripts/anonymized-curriculum-access-07-2021.txt", 
                     sep="\s", 
                     header=None, 
                     names = colnames, 
                     usecols=[0, 2, 3, 4, 5])
    df.date = pd.to_datetime(df.date)
    df = df.set_index(df.date)
    pages = df['endpoint'].resample('d').count()
    pages.head()
    df = df.set_index('date')
    
    return df