# Question: Hit Count
# Categories: 7 Kyu

def counter_effect(hit_count: str) -> list[list[int]]:
    result = []

    for i in range(len(hit_count)):
        count = []

        for j in range(0, int(hit_count[i]) + 1):
            count.append(j)
        
        result.append(count)
    
    return result