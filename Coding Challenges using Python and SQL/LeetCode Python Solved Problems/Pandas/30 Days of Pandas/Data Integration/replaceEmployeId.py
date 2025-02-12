# 1378.) Replace Employee ID With The Unique Identifier
# Categories : Pandas

import pandas as pd

def replace_employee_id(employees: pd.DataFrame, employee_uni: pd.DataFrame) -> pd.DataFrame:
    output_dict = {'unique_id' : [], 'name' : []}
    employee_uni_dict = {}
    
    for _, row in employee_uni.iterrows():
        employee_uni_dict[row.get('id')] = row.get('unique_id')

    for _, row in employees.iterrows():
        id = row.get('id')
        name = row.get('name')

        if id in employee_uni_dict:
            output_dict['unique_id'].append(employee_uni_dict[id])
            output_dict['name'].append(name)
        
        else:
            output_dict['unique_id'].append(None)
            output_dict['name'].append(name)
    
    return pd.DataFrame(output_dict)
        