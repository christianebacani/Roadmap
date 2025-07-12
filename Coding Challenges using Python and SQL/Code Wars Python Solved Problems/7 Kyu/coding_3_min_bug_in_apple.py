# Question: Coding 3min: Bug in Apple
# Categories: 7 Kyu

def sc(apple: list[list[str]]) -> tuple[int]:
    row_of_bug = None
    column_of_bug = None

    for i in range(len(apple)):
        if 'B' not in apple[i]:
            continue
        
        row_of_bug = i
        column_of_bug = apple[i].index('B')
        break

    return (row_of_bug, column_of_bug)