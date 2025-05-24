# Question: Scrabble Score
# Categories: 7 Kyu

def scrabble_score(st: str) -> int: 
    letters_and_score = {
        tuple(['A', 'E', 'I', 'O', 'U', 'L', 'N', 'R', 'S', 'T']): 1,
        tuple(['D', 'G']): 2,
        tuple(['B', 'C', 'M', 'P']): 3,
        tuple(['F', 'H', 'V', 'W', 'Y']): 4,
        tuple(['K']): 5,
        tuple(['J', 'X']): 8,
        tuple(['Q', 'Z']): 10
    }
    total = 0

    for i in range(len(st)):
        if not st[i].isalpha():
            continue

        for letters, score in letters_and_score.items():
            if st[i].upper() in letters:
                total += score
    
    return total