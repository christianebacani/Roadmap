# Question: Weird Algorithm

n = int(input().strip())
execution_of_the_algorithm = [n]

while n > 1:
    if n % 2 == 0:
        n = n // 2
        execution_of_the_algorithm.append(n)
    
    else:
        n *= 3
        n += 1
        execution_of_the_algorithm.append(n)

print(' '.join([str(num) for num in execution_of_the_algorithm]))