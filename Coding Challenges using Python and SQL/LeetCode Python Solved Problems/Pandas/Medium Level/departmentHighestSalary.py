# 184.) Department Highest Salary
# Categories : Pandas

import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    output_df = pd.DataFrame(columns=['Department', 'Employee', 'Salary'])

    for _, row in department.iterrows():
        department_id = row.get('id')
        department_name = row.get('name')

        salaries_per_department = {department_id : []}
        
        for _, inner_row in employee.iterrows():
            salary = inner_row.get('salary')
            employee_department_id = inner_row.get('departmentId')

            if department_id == employee_department_id:
                salaries_per_department[department_id].append(salary)
        
        highest_salary = max(salaries_per_department[department_id], default=0)

        for _, inner_row in employee.iterrows():
            name = inner_row.get('name')
            salary = inner_row.get('salary')
            employee_department_id = inner_row.get('departmentId')

            if (department_id == employee_department_id) and (salary == highest_salary):
                output_df = pd.concat([output_df, pd.DataFrame({'Department' : department_name, 'Employee' : name, 'Salary' : salary}, index=[0])], ignore_index=True)

    return output_df
