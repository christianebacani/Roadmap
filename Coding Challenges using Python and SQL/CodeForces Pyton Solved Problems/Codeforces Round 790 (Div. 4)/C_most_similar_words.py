# C - Most Similar Words

def difference_of_two_word(first_word: str, second_word: str) -> int:
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    total_difference = 0

    for i in range(len(first_word)):
        difference = abs((alphabet.index(first_word[i]) + 1) - (alphabet.index(second_word[i]) + 1))
        total_difference += difference
    
    return total_difference

t = int(input().strip())

for _ in range(t):
    first_line = input().strip().split()
    n = int(first_line[0])
    m = int(first_line[1])
    word = []

    for _ in range(n):
        word.append(input().strip())
    
    differences = []

    for i in range(len(word)):
        for j in range(len(word)):
            if i >= j:
                continue

            differences.append(difference_of_two_word(word[i], word[j]))
    
    answer = min(differences, default=0)
    print(answer)