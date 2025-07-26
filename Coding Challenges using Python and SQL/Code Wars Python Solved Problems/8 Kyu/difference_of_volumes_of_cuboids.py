# Question: Difference of Volumes of Cuboids
# Categories: 8 Kyu

def find_difference(a: list[int], b: list[int]) -> int:
    volume_of_a = 1
    volume_of_b = 1

    for i in range(len(a)):
        volume_of_a *= a[i]

    for i in range(len(b)):
        volume_of_b *= b[i]

    answer = abs(volume_of_a - volume_of_b)
    return answer