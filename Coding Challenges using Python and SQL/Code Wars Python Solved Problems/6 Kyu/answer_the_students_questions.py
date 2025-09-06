# Question: Answer the students' questions!
# Categories: 6 Kyu

def answer(question: str, information: list[str]) -> str | None:
    question = question.split()
    number_of_common_words_per_info = []

    for i in range(len(information)):
        info = information[i].lower().split()
        total = 0

        for j in range(len(info)):
            if info[j] in question:
                total += 1
        
        number_of_common_words_per_info.append(total)
    
    if max(number_of_common_words_per_info) == 0:
        return None

    result_index = number_of_common_words_per_info.index(max(number_of_common_words_per_info))
    return information[result_index]