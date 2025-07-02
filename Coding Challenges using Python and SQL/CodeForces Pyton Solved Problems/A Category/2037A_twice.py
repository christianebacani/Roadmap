# 2037A - Twice

t = int(input().strip())

for _ in range(t):
    n = int(input().strip())
    a = input().strip().split()
    a = [int(num) for num in a]

    selected_indices_for_operation = []
    total_score = 0

    for i in range(len(a)):
        for j in range(len(a)):
            if i >= j:
                continue

            if i in selected_indices_for_operation or j in selected_indices_for_operation:
                continue
            
            if a[i] != a[j]:
                continue
            
            selected_indices_for_operation.append(i)
            selected_indices_for_operation.append(j)
            total_score += 1
    
    answer = total_score
    print(answer)