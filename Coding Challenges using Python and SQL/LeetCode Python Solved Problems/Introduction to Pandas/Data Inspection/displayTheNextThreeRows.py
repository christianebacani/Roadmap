# 2879. Display the First Three Rows
# Category : Pandas

import pandas as pd

def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    indicesToRemove = []

    for index, _ in enumerate(employees['employee_id']):        
        if index > 2:
            indicesToRemove.append(index)
    
    employees.drop(index=indicesToRemove, inplace=True)

    return employees