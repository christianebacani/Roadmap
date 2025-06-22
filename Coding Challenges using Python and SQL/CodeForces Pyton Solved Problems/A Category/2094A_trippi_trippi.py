# 2094A - Trippi Troppi

number_of_test_cases = int(input().strip())

for _ in range(number_of_test_cases):
    ancient_country_name = input().strip().split()
    modern_name = ''

    for i in range(len(ancient_country_name)):
        modern_name += ancient_country_name[i][0]

    print(modern_name)