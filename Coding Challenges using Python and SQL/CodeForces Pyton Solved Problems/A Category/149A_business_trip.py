# 149A - Business trip

k = int(input().strip())
centimeters = input().strip().split()
centimeters = [int(centimeter) for centimeter in centimeters]
centimeters.sort()
centimeters.reverse()

list_of_number_of_months_that_satisfies_conditions = []

for i in range(len(centimeters) + 1):
    for j in range(len(centimeters)):
        subarray = centimeters[j : j + i]
        
        if len(subarray) != i:
            continue

        if sum(subarray) >= k:
            list_of_number_of_months_that_satisfies_conditions.append(len(subarray))

print(min(list_of_number_of_months_that_satisfies_conditions, default=-1))