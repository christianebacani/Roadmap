# 176.) Second Highest Salary
# Categories : Pandas

import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    second_highest_salary_dict = {'SecondHighestSalary' : [None]}
    employee_salaries = []
    

    for _, row in employee.iterrows():
        salary = row.get('salary')

        if salary not in employee_salaries:
            employee_salaries.append(salary)
    
    employee_salaries = sorted(employee_salaries, reverse=True)


    for index, salary in enumerate(employee_salaries):
        index += 1

        if index == 2:
            second_highest_salary_dict['SecondHighestSalary'] = [salary]
    
    second_highest_salary_df = pd.DataFrame(second_highest_salary_dict)

    return second_highest_salary_df

