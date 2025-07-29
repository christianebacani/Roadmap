'''
    SQL Query Module
'''
import pandas as pd
import snowflake.connector

def test_sql_query(query: str) -> pd.DataFrame:
    '''
        Test SQL Query Function
    '''
    conn = snowflake.connector.connect(
        user='<SNOWFLAKE_USERNAME>',
        password='<SNOWFLAKE_PASSWORD>',
        account='<SNOWFLAKE_ACCOUNT_IDENTIFIER>',
        warehouse='san_francisco_budget_data_warehouse',
        database='san_francisco_budget_data',
        schema='san_francisco_budget_data_star_schema'
    )
    # Initialize a snowflake cursor for executing SQL queries
    cursor = conn.cursor()

    # TODO: Implement more functionalities here...