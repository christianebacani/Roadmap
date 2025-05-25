# Question: String array duplicates
# Categories: 6 Kyu

def dup(arr: list[str]) -> list[str]:
    result = []

    for i in range(len(arr)):
        word = arr[i]
        stack = []

        for j in range(len(word)):
            if stack == []:
                stack.append(word[j])
                continue

            if stack[-1] != word[j]:
                stack.append(word[j])
        
        result.append(''.join(stack))
    
    return result