# 1385B - Restore the Permutation by Merger

t = int(input().strip())

for _ in range(t):
    n = input()
    permutation = input().strip().split()
    permutation = [int(num) for num in permutation]
    answer = []

    for i in range(len(permutation)):
        if permutation[i] not in answer:
            answer.append(permutation[i])
    
    answer = ' '.join([str(num) for num in answer])
    print(answer)