# 2881. Create a New Column
# Category : Pandas

import pandas as pd

def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employeesWithBonusDict = {'name' : [], 'salary' : [], 'bonus' : []}
    
    for _, row in employees.iterrows():
        name = row.get('name', None)
        salary = row.get('salary', None)
        bonus = int(salary) * 2
        
        employeesWithBonusDict['name'].append(name)
        employeesWithBonusDict['salary'].append(salary)
        employeesWithBonusDict['bonus'].append(bonus)

    employeesWithBonusDf = pd.DataFrame(employeesWithBonusDict)

    return employeesWithBonusDf