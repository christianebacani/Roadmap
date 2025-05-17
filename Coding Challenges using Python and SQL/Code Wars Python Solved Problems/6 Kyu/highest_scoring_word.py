# Question: Highest Scoring Word
# Categories: 6 Kyu

def high(x: str) -> str:
    alphabets = 'abcdefghijklmnopqrstuvwxyz'
    x = x.split()
    scores = []

    for i in range(len(x)):
        score = 0

        for j in range(len(x[i])):
            score += (alphabets.index(x[i][j]) + 1)

        scores.append(score)
    
    return x[scores.index(max(scores))]