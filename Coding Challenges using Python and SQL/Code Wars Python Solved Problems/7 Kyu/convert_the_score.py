# Question: Convert the score
# Categories: 7 Kyu

def scoreboard(score_string: str) -> list[int]:
    words_to_digit = {
        'nil': 0,
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9
    }

    score_string = score_string.split()
    result = []

    for i in range(len(score_string)):
        score_string[i] = score_string[i].strip().lower()
        
        if score_string[i] not in words_to_digit:
            continue
        
        result.append(words_to_digit[score_string[i]])
    
    return result