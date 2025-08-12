# Question: Least Larger
# Categories: 7 Kyu

def least_larger(a: list[int], i: int) -> int: 
    indices_and_element_with_distance = {}

    for index, element in enumerate(a):
        if element > a[i]:
            indices_and_element_with_distance[index] = [element, abs(element - a[i])]
    
    if indices_and_element_with_distance == {}:
        return -1

    distances = []

    for index, element_with_distance in indices_and_element_with_distance.items():
        distances.append(element_with_distance[1])
    
    min_distance = min(distances)

    for index, element_with_distance in indices_and_element_with_distance.items():
        if min_distance == element_with_distance[1]:
            return index