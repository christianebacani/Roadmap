# Question: Word values
# Categories: 7 Kyu

def name_value(my_list: list[str]) -> list[int]:
    alphabets = 'abcdefghijklmnopqrstuvwxyz'
    result = []

    for i in range(len(my_list)):
        word = my_list[i]
        sum = 0

        for j in range(len(word)):
            if not word[j].isalpha():
                continue
            
            sum += (alphabets.index(word[j]) + 1)

        result.append(sum * (i + 1))
    
    return result