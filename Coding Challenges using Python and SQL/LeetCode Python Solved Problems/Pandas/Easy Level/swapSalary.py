# 627.) Swap Salary
# Categories : Pandas

import pandas as pd

def swap_salary(salary: pd.DataFrame) -> pd.DataFrame:
    swap_sex_salary_df = pd.DataFrame(columns=['id', 'name', 'sex', 'salary'])
    
    for _, row in salary.iterrows():
        id = row.get('id')
        name = row.get('name')
        sex = row.get('sex')
        salary_column = row.get('salary')

        if sex == 'm':
            sex = 'f'
        
        else:
            sex = 'm'
        
        swap_sex_salary_df = pd.concat([swap_sex_salary_df, pd.DataFrame({'id' : [id],
                                                                          'name' : [name],
                                                                          'sex' : [sex],
                                                                          'salary' : [salary_column]})], ignore_index=True)
    
    return swap_sex_salary_df