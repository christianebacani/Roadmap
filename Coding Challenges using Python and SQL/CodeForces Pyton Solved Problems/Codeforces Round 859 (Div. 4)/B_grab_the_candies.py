# B - Grab the Candies

t = int(input().strip())

for _ in range(t):
    n = input()
    bags_of_candies = input().strip().split()
    bags_of_candies = [int(bag_of_candies) for bag_of_candies in bags_of_candies]

    even_number_of_bags_of_candies, odd_number_of_bags_of_candies = [], []

    for i in range(len(bags_of_candies)):
        if bags_of_candies[i] % 2 == 0:
            even_number_of_bags_of_candies.append(bags_of_candies[i])
        
        else:
            odd_number_of_bags_of_candies.append(bags_of_candies[i])
    
    if sum(even_number_of_bags_of_candies) > sum(odd_number_of_bags_of_candies):
        print('YES')
    
    else:
        print('NO')