# Question: Find the Mine!
# Categories: 6 Kyu

def mine_location(field: list[list[int]]) -> list[int]:
    answer = []

    for i in range(len(field)):
        if 1 not in field[i]:
            continue

        column_pos_of_mine = field[i].index(1)
        answer.append(i)
        answer.append(column_pos_of_mine)
        break

    return answer