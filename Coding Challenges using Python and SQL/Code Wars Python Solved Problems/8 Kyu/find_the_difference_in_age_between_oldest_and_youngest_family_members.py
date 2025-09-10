# Question: Find the Difference in Age between Oldest and Youngest Family Members
# Categories: 8 Kyu

def difference_in_ages(ages: list[int]) -> list[int]:
    return tuple([min(ages), max(ages), max(ages) - min(ages)])