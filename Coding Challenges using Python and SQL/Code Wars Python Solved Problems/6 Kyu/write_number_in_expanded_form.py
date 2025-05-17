# Question: Write Number in Expanded Form
# Categories: 6 Kyu

def expanded_form(num: int) -> str:
    num = str(num)
    answer = []

    for i in range(len(num)):
        current_number = num[i]

        if current_number == '0':
            continue

        current_number = current_number + (len(num[i + 1:]) * '0')
        answer.append(current_number)
    
    answer = ' + '.join(answer)

    return answer