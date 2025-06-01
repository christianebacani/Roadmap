# Question: SevenAte9
# Categories: 7 Kyu

def seven_ate9(digits: str) -> str:
    result = ''

    for i in range(len(digits)):
        if digits[i] != '9':
            result += digits[i]
            continue
        
        try:
            if digits[i - 1] == '7' and digits[i + 1] == '7':
                continue
        
            result += digits[i]

        except:
            result += digits[i]

    return result