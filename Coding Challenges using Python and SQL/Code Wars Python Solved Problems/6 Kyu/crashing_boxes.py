# Question: Crashing Boxes
# Categories: 6 Kyu

def crashing_weights(weights: list[int] | list[list[int]]) -> list[int]:
    if len(weights) == 1:
        return weights[0]
    
    for i in range(1, len(weights)):
        previous_weight = weights[i - 1]
        current_weight = weights[i]

        for j in range(len(current_weight)):
            if previous_weight[j] > current_weight[j]:
                current_weight[j] = previous_weight[j] + current_weight[j]
        
        weights[i] = current_weight

    return weights[-1]