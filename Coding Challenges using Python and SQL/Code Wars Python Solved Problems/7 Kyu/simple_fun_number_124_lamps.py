# Question: Simple Fun #124: Lamps
# Categories: 7 Kyu

def lamps(a: list[int]) -> int:
    alternate_lamps1 = []
    alternate_lamps2 = []

    for i in range(len(a)):
        if i % 2 == 0:
            alternate_lamps1.append(1)
            alternate_lamps2.append(0)

        else:
            alternate_lamps1.append(0)
            alternate_lamps2.append(1)
    
    number_of_lamps_to_swich_in_lamps1, number_of_lamps_to_swich_in_lamps2 = 0, 0

    for i in range(len(alternate_lamps1)):
        if alternate_lamps1[i] != a[i]:
            number_of_lamps_to_swich_in_lamps1 += 1

    for i in range(len(alternate_lamps2)):
        if alternate_lamps2[i] != a[i]:
            number_of_lamps_to_swich_in_lamps2 += 1
    
    return min([number_of_lamps_to_swich_in_lamps1, number_of_lamps_to_swich_in_lamps2])