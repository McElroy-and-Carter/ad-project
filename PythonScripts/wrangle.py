import numpy as np
import pandas as pd
import warnings
warnings.filterwarnings('ignore')
from PythonScripts.env import host, user ,password
from sklearn.model_selection import train_test_split
import os


###################### Getting database Url ################
def get_db_url(db_name, user=user, host=host, password=password):
    """
        This helper function takes as default the user host and password from the env file.
        You must input the database name. It returns the appropriate URL to use in connecting to a database.
    """
    url = f'mysql+pymysql://{user}:{password}@{host}/{db_name}'
    return url
######################### get generic data #########################
def get_any_data(database, sql_query):
    '''
    put in the query and the database and get the data you need in a dataframe
    '''
    return pd.read_sql(sql_query, get_db_url(database))




def get_curriculum_log():
    colnames = ['date', 'endpoint', 'user_id', 'cohort_id', 'source_ip']
    df = pd.read_csv("PythonScripts/anonymized-curriculum-access-07-2021.txt", 
                     sep="\s", 
                     header=None, 
                     names = colnames, 
                     usecols=[0, 2, 3, 4, 5])
    
    df2 = get_any_data('curriculum_logs','select * from cohorts')
    
    df = df.merge(df2, left_on='cohort_id', right_on='id')
    
    df = df.drop(columns = ['id','slack','deleted_at'])
    
    df.date = pd.to_datetime(df.date)
    df = df.set_index(df.date)
    pages = df['endpoint'].resample('d').count()
    df = df.set_index('date')
    
    
    
    return df