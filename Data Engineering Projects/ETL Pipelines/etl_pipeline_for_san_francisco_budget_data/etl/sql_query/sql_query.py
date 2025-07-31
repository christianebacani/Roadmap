'''
    SQL Query Module
'''
import pandas as pd
from sqlalchemy import create_engine
from snowflake.sqlalchemy import URL

def test_sql_query(query: str) -> pd.DataFrame | str:
    '''
        Test SQL Query Function
    '''
    # Perform SQL Query Testing using SQL Alchemy Engine
    engine = create_engine(URL(
        user='<SNOWFLAKE_USERNAME>',
        password='<SNOWFLAKE_PASSWORD>',
        account='<SNOWFLAKE_ACCOUNT_IDENTIFIER>',
        database='san_francisco_budget_data',
        schema='san_francisco_budget_data_star_schema',
        warehouse='san_francisco_budget_data_warehouse'
    ))
    
    try:
        dataframe = pd.read_sql(query, engine)
        return dataframe

    except Exception as error_message:
        return f'Error message: {error_message}'