# 1980A - Problem Generator

t = int(input().strip())

for _ in range(t):
    test_input = input().strip().split()
    n = int(test_input[0])
    m = int(test_input[1])

    difficulties_in_the_bank = input()
    total = 0

    for _ in range(m):
        difficulties = 'ABCDEFG'

        for i in range(len(difficulties)):
            if difficulties[i] not in difficulties_in_the_bank:
                total += 1
            
            else:
                target_index = difficulties_in_the_bank.index(difficulties[i])
                difficulties_in_the_bank = difficulties_in_the_bank[:target_index] + difficulties_in_the_bank[target_index + 1:]
    
    print(total)