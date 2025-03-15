'''
    Run queries
'''
import pandas as pd
from database_connection.database_connection import connect

def queries() -> None:
    '''
        Run query function to run queries from the database server
    '''
    # Using connect function from database connection package to provide connection
    engine = connect()

    # Run queries using pandas from the table of the server to test if the datasets are correctly stored in the server
    education_est_2021 = pd.read_sql('SELECT * FROM education_est_2021', engine)
    print(f'\neducation_est_2021:')
    print(education_est_2021)
    print()
    
    wholesale_and_retail_trade_2015 = pd.read_sql('SELECT * FROM wholesale_and_retail_trade_2015', engine)
    print(f'wholesale_and_retail_trade_2015:')
    print(wholesale_and_retail_trade_2015)
    print()
    
    prof_scientific_and_tech_acts_est_2019 = pd.read_sql('SELECT * FROM prof_scientific_and_tech_acts_est_2019', engine)
    print(f'prof_scientific_and_tech_acts_est_2019:')
    print(prof_scientific_and_tech_acts_est_2019)

    

        