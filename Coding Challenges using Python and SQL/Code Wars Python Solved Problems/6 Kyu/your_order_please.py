# Question: Your order, please
# Categories: 6 Kyu

def order(sentence: str) -> str:
    if sentence == '':
        return ''

    sentence = sentence.split()
    answer = []

    for i in range(1, 10):
        for j in range(len(sentence)):
            if str(i) in sentence[j]:
                answer.append(sentence[j])
                break
    
    return ' '.join(answer)