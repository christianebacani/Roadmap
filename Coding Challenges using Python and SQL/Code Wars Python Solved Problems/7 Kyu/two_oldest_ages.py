# Question: Two Oldest Ages
# Categories: 7 Kyu

def two_oldest_ages(ages: list[int]) -> list[int]:
    ages.sort()
    ages.reverse()

    return [ages[1], ages[0]]