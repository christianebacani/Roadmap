'''
    Provide database connection
'''
import sqlalchemy

def connect() -> sqlalchemy.Engine:
    '''
        Database connection function to provide database connection
    '''
    username = '<YOUR_USERNAME>'
    password = '<YOUR_PASSWORD>'
    hostname = '<YOUR_HOSTNAME>'
    port = '<YOUR_PORT_NUMBER>'
    database = 'psa_summary_stats'
    
    conn = sqlalchemy.create_engine(f'postgresql://{username}:{password}@{hostname}:{port}/{database}')
    return conn
