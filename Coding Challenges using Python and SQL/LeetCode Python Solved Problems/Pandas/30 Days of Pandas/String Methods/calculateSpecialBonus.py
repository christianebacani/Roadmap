# 1873.) Calculate Special Bonus
# Categories : Pandas

import pandas as pd

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    employeesWithBonusDict = {'employee_id' : [], 'bonus' : []}
    
    for _, row in employees.iterrows():
        employeeId = int(row.get('employee_id'))
        name = str(row.get('name'))
        salary = int(row.get('salary'))

        employeesWithBonusDict['employee_id'].append(employeeId)
            
        if (employeeId % 2 == 1) and (name[:1] != 'M'):
            employeesWithBonusDict['bonus'].append(salary)
        
        else:
            employeesWithBonusDict['bonus'].append(0)
    

    employeesWithBonusDf = pd.DataFrame(employeesWithBonusDict)
    sortedEmployeesWithBonus = employeesWithBonusDf.sort_values(by=['employee_id'])
    
    return sortedEmployeesWithBonus