# Question: Genetic Algorithm Series - #3 Crossover
# Categories: 7 Kyu

def crossover(chromosome1: str, chromosome2: str, index: int) -> list[str]:
    chromosome1_part = chromosome1[index:]
    chromosome2_part = chromosome2[index:]

    chromosome1 = chromosome1[:index] + chromosome2_part
    chromosome2 = chromosome2[:index] + chromosome1_part

    return [chromosome1, chromosome2]