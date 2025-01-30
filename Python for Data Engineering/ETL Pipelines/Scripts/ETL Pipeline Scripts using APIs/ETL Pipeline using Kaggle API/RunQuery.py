import pandas as pd

# Run Query at Local SQLite Database

def run_query(query, conn):
    queryDf = pd.read_sql(query, conn)
    return queryDf