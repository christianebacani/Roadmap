# 1854.) Maximum Population Year
# Categories: Array, Counting, Prefix Sum

class Solution:
    def maximumPopulation(self, logs: list[list[int]]) -> int:
        birth_years = []
        death_years = []

        for i in range(len(logs)):
            birth_years.append(logs[i][0])
            death_years.append(logs[i][1])
        
        minimum_year = min(birth_years)
        maximum_year = max(death_years) - 1
        
        year_and_number_of_populations = {}

        for i in range(minimum_year, maximum_year + 1):
            number_of_populations = 0

            for j in range(len(logs)):
                if i in range(logs[j][0], logs[j][1]):
                    number_of_populations += 1
            
            year_and_number_of_populations[i] = number_of_populations
        
        maximum_number_of_populations = max(list(year_and_number_of_populations.values()))

        for year, number_of_populations in year_and_number_of_populations.items():
            if maximum_number_of_populations == number_of_populations:
                return year