# Question: Sum of a sequence
# Categories: 7 Kyu

def sequence_sum(begin_number, end_number, step):
    return sum([num for num in range(begin_number, end_number + 1, step)])