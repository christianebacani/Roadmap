# 1669C - Odd/Even Increments

t = int(input().strip())

for _ in range(t):
    n = int(input().strip())
    elements_of_the_array = input().strip().split()
    elements_of_the_array = [int(num) for num in elements_of_the_array]

    odd_indexed_elements, even_indexed_elements = [], []

    for i in range(len(elements_of_the_array)):
        if (i + 1) % 2 != 0:
            odd_indexed_elements.append(elements_of_the_array[i])
        
        else:
            even_indexed_elements.append(elements_of_the_array[i])
    
    total_odd_elements_in_odd_indexed_elements, total_even_elements_in_odd_indexed_elements = 0, 0

    for i in range(len(odd_indexed_elements)):
        if odd_indexed_elements[i] % 2 != 0:
            total_odd_elements_in_odd_indexed_elements += 1
        
        else:
            total_even_elements_in_odd_indexed_elements += 1
    
    if (total_odd_elements_in_odd_indexed_elements != 0) and (total_odd_elements_in_odd_indexed_elements != len(odd_indexed_elements)):
        print('NO')
        continue

    else:
        pass
    
    if (total_even_elements_in_odd_indexed_elements != 0) and (total_even_elements_in_odd_indexed_elements != len(odd_indexed_elements)):
        print('NO')
        continue
    
    else:
        pass

    total_odd_elements_in_even_indexed_elements, total_even_elements_in_even_indexed_elements = 0, 0

    for i in range(len(even_indexed_elements)):
        if even_indexed_elements[i] % 2 != 0:
            total_odd_elements_in_even_indexed_elements += 1
        
        else:
            total_even_elements_in_even_indexed_elements += 1
    
    if (total_odd_elements_in_even_indexed_elements != 0) and (total_odd_elements_in_even_indexed_elements != len(even_indexed_elements)):
        print('NO')
        continue

    else:
        pass

    if (total_even_elements_in_even_indexed_elements != 0) and (total_even_elements_in_even_indexed_elements != len(even_indexed_elements)):
        print('NO')
    
    else:
        pass

    print('YES')