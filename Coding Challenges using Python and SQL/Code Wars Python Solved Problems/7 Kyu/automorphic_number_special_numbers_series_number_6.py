# Question: Automorphic Number (Special Numbers Series #6)
# Categories: 7 Kyu

def automorphic(n: int) -> str:
    square = str(n ** 2)
    print(square)

    if square.endswith(str(n)):
        return 'Automorphic'
    
    return 'Not!!'