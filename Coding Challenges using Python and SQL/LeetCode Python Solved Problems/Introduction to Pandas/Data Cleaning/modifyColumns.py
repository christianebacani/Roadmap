# 2884.) Modify Columns
# Category : Pandas

import pandas as pd

def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
    doubledSalaryEmployeesDict = {'name' : [], 'salary' : []}

    for _, row in employees.iterrows():
        name = str(row.get('name'))
        doubledSalary = int(row.get('salary')) * 2

        doubledSalaryEmployeesDict['name'].append(name)
        doubledSalaryEmployeesDict['salary'].append(doubledSalary)

    doubledSalaryEmployeesDf = pd.DataFrame(doubledSalaryEmployeesDict)

    return doubledSalaryEmployeesDf