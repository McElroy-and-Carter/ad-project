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
    df.loc[df['program_id'] == 1, 'program_name'] = 'PHP'
    df.loc[df['program_id'] == 2, 'program_name'] = 'Java'
    df.loc[df['program_id'] == 3, 'program_name'] = 'Data Science' 
    df.loc[df['program_id'] == 4, 'program_name'] = 'Front End'
    
    df = df.dropna()
    
    df.start_date = pd.to_datetime(df.start_date)
    df.end_date = pd.to_datetime(df.end_date)
    df.created_at =pd.to_datetime(df.created_at)
    df.updated_at =pd.to_datetime(df.updated_at)
    df.date = pd.to_datetime(df.date)
    df = df.set_index(df.date)
    pages = df['endpoint'].resample('d').count()
    df = df.set_index('date')

    
    
    
    return df

def get_lower_and_upper_bounds(df, k=1.5):
    '''
    calculates the lower and upper bound to locate outliers and displays them
    note: recommended k be 1.5
    '''
    for i in df.columns:
        if df[i].dtypes != 'object':
            quartile1, quartile3 = np.percentile(df[i], [25,75])
            IQR_value = quartile3 - quartile1
            lower_bound = (quartile1 - (k * IQR_value))
            upper_bound = (quartile3 + (k * IQR_value))
            print('------------------------------------------------------')
            print(f'For {i} the lower bound is {lower_bound} and  upper bound is {upper_bound}')
            outliers_lower = df[df[i] < lower_bound]
            outliers_upper = df[df[i] > upper_bound]
            outliers = pd.concat([outliers_lower, outliers_upper], axis=0)
            print('')
            print(outliers,'\n')
    else:
        print('')