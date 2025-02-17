# 1965.) Employees With Missing Information
# Categories : Pandas

import pandas as pd

def find_employees(employees: pd.DataFrame, salaries: pd.DataFrame) -> pd.DataFrame:
    output_df = pd.DataFrame(columns=['employee_id'])
    employee_ids = list(employees['employee_id'])
    employee_ids.extend(list(salaries['employee_id']))

    employee_ids = sorted(list(set(employee_ids)))

    for employee_id in employee_ids:
        if employee_id not in list(employees['employee_id']):
            output_df = pd.concat([output_df, pd.DataFrame({'employee_id' : employee_id}, index=[0])], ignore_index=True)
        
        elif employee_id not in list(salaries['employee_id']):
            output_df = pd.concat([output_df, pd.DataFrame({'employee_id' : employee_id}, index=[0])], ignore_index=True)
    
    output_df.sort_values(by=['employee_id'], ascending=[True], inplace=True)

    return output_df