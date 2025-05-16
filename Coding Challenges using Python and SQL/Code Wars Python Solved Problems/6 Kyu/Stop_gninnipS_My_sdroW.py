# Question: Stop gninnipS My sdroW!
# Categories: 6 Kyu

def spin_words(sentence: str) -> str:
    sentence = sentence.split()
    answer = []
    
    for i in range(len(sentence)):
        if len(sentence[i]) < 5:
            answer.append(sentence[i])
        
        else:
            answer.append(sentence[i][::-1])
    
    answer = ' '.join(answer)
    
    return answer