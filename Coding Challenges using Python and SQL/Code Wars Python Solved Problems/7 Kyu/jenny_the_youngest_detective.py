# Question: Jenny the youngest detective
# Categories: 7 Kyu

def missing(codes: list[int], sentence: str) -> str:
    new_sentence = ''

    for i in range(len(sentence)):
        if sentence[i] != ' ':
            new_sentence += sentence[i]
    
    codes.sort()
    sentence = new_sentence
    result = ''

    for i in range(len(codes)):
        try:
            result += sentence[codes[i]].lower()

        except IndexError:
            return 'No mission today'
    
    return result