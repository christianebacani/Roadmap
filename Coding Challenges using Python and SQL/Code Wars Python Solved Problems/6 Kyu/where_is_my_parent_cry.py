# Question: Where is my parent?(cry)
# Categories: 6 Kyu

def find_children(dancing_brigade: str) -> str:
    mothers = []

    for i in range(len(dancing_brigade)):
        if dancing_brigade[i].isupper():
            mothers.append(dancing_brigade[i])
    
    mothers = sorted(mothers)
    result = ''

    for i in range(len(mothers)):
        children = []

        for j in range(len(dancing_brigade)):
            if dancing_brigade[j].isupper():
                continue

            if mothers[i].lower() == dancing_brigade[j]:
                children.append(dancing_brigade[j])
        
        result += mothers[i]
        result += (''.join(children))

    return result