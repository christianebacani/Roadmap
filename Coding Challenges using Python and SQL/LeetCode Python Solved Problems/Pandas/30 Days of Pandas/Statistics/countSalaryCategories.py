# 1907.) Count Salary Categories
# Categories : Pandas

import pandas as pd

def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    salary_categories = {'category' : ['Low Salary', 'Average Salary', 'High Salary'], 
                         'accounts_count' : None}
    
    low_salary_count = 0
    average_salary_count = 0
    high_salary_count = 0

    for _, row in accounts.iterrows():
        income = row.get('income')

        if income < 20000:
            low_salary_count += 1
        
        elif (income >= 20000) and (income <= 50000):
            average_salary_count += 1
        
        else:
            high_salary_count += 1
    
    salary_categories['accounts_count'] = [low_salary_count, average_salary_count, high_salary_count]
    salary_categories_df = pd.DataFrame(salary_categories)

    return salary_categories_df
    
    