# 1676B - Equal Candies

t = int(input().strip())

for _ in range(t):
    n = input().strip()
    quantities_of_candies_per_box = input().strip().split()
    quantities_of_candies_per_box = [int(quantity) for quantity in quantities_of_candies_per_box]

    minimum_quantity = min(quantities_of_candies_per_box)
    minimum_number_of_candies_to_eat = 0

    for i in range(len(quantities_of_candies_per_box)):
        minimum_number_of_candies_to_eat += (abs(quantities_of_candies_per_box[i] - minimum_quantity))
    
    print(minimum_number_of_candies_to_eat)