'''
    Read Module
'''
from src.utils.utils import init_engine

def get_table_names_from_postgresql_db() -> list[str]:
    '''
        Get function to extract all table names
        from PostgreSQL Database
    '''
    engine = init_engine()
    
def read_table_main_page() -> None:
    '''
        CLI-Based Main Page for Reading Tables
    '''
    while True:
        header = 'Read Tables'
        print(f'\t\t{header}\n')