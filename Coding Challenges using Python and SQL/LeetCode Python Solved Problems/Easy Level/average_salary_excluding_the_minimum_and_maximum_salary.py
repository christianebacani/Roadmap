# 1491.) Average Salary Excluding the Minimum and Maximum Salary
# Categories: Array, Sorting

class Solution:
    def average(self, salary: list[int]) -> float:
        maximum_salary = max(salary)
        minimum_salary = min(salary)
        
        total_salary = 0
        number_of_salaries = 0
        
        for i in range(len(salary)):
            if salary[i] == minimum_salary or salary[i] == maximum_salary:
                continue

            total_salary += salary[i]
            number_of_salaries += 1
        
        return round(total_salary / number_of_salaries, 5)