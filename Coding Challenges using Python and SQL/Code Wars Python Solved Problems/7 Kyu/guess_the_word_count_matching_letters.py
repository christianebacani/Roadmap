# Question: Guess the Word: Count Matching Letters
# Categories: 7 Kyu

def count_correct_characters(correct: str, guess: str) -> int:
    if len(correct) != len(guess):
        raise Exception
    
    total = 0

    for i in range(len(guess)):
        if guess[i] == correct[i]:
            total += 1
    
    return total