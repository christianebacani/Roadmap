'''
    Test SQL Query Module
'''
import pandas as pd
from sqlalchemy import create_engine

def run_sql_query() -> None:
    '''
        SQL Query function to
        run SQL Query from PostgreSQL
        Database Server with the use of
        SQLAlchemy Engine
    '''
    username = '<YOUR_USERNAME_CREDENTIALS_FOR_POSTGRESQL_DB_SERVER>'
    password = '<YOUR_PASSWORD_CREDENTIALS_FOR_POSTGRESQL_DB_SERVER>'
    hostname = '<YOUR_OWN_SPECIFIC_HOSTNAME>'
    port = '5432'
    database = 'ph_family_income_and_expenditure_surveys'

    engine = create_engine(f'postgresql://{username}:{password}@{hostname}:{port}/{database}')

    share_to_total_fam_expend = pd.read_sql('SELECT * FROM share_to_total_fam_expend WHERE share_to_total_fam_expend_in_pct_2018 <> 0', engine)
    avg_annual_fam_expenditure_per_capita = pd.read_sql('SELECT * FROM avg_annual_fam_expenditure_per_capita', engine)
    gini_coefficient_and_palma_ratio = pd.read_sql('SELECT * FROM gini_coefficient_and_palma_ratio', engine)

    print(f'Table Name: share_to_total_fam_expend:')
    print(share_to_total_fam_expend)
    print()

    print(f'Table Name: avg_annual_fam_expenditure_per_capita')
    print(avg_annual_fam_expenditure_per_capita)
    print()

    print(f'Table Name: gini_coefficient_and_palma_ratio')    
    print(gini_coefficient_and_palma_ratio)