# Question: Growth of a Population
# Categories: 7 Kyu
import math

def nb_year(current_num_of_population: int, percentage_growth: int, number_of_people_come_per_year: int, population_threshold: int) -> int:
    percentage_growth = percentage_growth * 0.01
    total_number_of_years = 0

    while current_num_of_population < population_threshold:
        current_num_of_population += ((current_num_of_population * percentage_growth) + number_of_people_come_per_year)
        current_num_of_population = math.floor(current_num_of_population)
        total_number_of_years += 1
    
    return total_number_of_years