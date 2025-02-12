# 1741.) Find Total Time Spent by Each Employee
# Categories : Pandas

import pandas as pd

def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    employee_total_time_spent = pd.DataFrame(columns=['day', 'emp_id', 'total_time'])
    employee_ids_day = {}


    for _, row in employees.iterrows():
        emp_id = row.get('emp_id')
        event_day = row.get('event_day')
        
        if (tuple([emp_id, event_day])) not in list(employee_ids_day.keys()):
            employee_ids_day[tuple([emp_id, event_day])] = None
    

    for key in list(employee_ids_day.keys()):
        total_time = 0

        for _, row in employees.iterrows():
            emp_id = row.get('emp_id')
            event_day = row.get('event_day')
            
            if key == tuple([emp_id, event_day]):
                total_time += row.get('out_time') - row.get('in_time')

        employee_ids_day[key] = total_time


    for key, value in employee_ids_day.items():
        employee_total_time_spent = pd.concat([employee_total_time_spent, pd.DataFrame({'day' : [key[1]],
                                                                                        'emp_id' : [key[0]],
                                                                                        'total_time' : [value]})], ignore_index=True)    

    return employee_total_time_spent