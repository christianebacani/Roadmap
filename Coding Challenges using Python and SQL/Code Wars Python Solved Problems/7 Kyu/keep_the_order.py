# Question: Keep the Order
# Categories: 7 Kyu

def keep_order(ary: list[int], val: int) -> int:
    ary.append(val)
    ary.sort()
    answer = ary.index(val)

    return answer