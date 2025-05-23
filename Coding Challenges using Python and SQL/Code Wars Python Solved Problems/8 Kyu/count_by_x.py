# Question: Count by X
# Categories: 8 Kyu

def count_by(multiple: int, total_number_of_elements: int) -> list[int]:
    elements = [i for i in range(1, 1001) if i % multiple == 0]

    return elements[:total_number_of_elements]