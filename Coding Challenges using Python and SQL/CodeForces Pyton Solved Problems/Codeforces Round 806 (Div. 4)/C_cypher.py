# C - Cypher

t = int(input().strip())

for _ in range(t):
    n = int(input().strip())
    sequence = input().strip().split()
    sequence = [int(num) for num in sequence]

    operations = []

    for _ in range(n):
        operations.append(input().strip().split()[1])
    
    for index, operation in enumerate(operations):
        for i in range(len(operation)):
            if operation[i] == 'U':
                if sequence[index] == 0:
                    sequence[index] = 9
                
                else:
                    sequence[index] = sequence[index] - 1
            
            else:
                if sequence[index] == 9:
                    sequence[index] = 0
                
                else:
                    sequence[index] = sequence[index] + 1
    
    sequence = [str(num) for num in sequence]
    sequence = ' '.join(sequence)

    print(sequence)