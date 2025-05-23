# Question: Sum of Odd Cubed Numbers
# Categories: 7 Kyu

def cube_odd(arr: list[int | None | bool | str]) -> int | None:
    sum_of_cubed_integers = 0

    for i in range(len(arr)):
        if isinstance(arr[i], (bool, str)):
            return None
    
    for i in range(len(arr)):
        if arr[i] % 2 != 0:
            sum_of_cubed_integers += (arr[i] ** 3)
    
    return sum_of_cubed_integers