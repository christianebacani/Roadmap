# Question: Unfinished Loop - Bug Fixing #1
# Categories: 8 Kyu

def create_array(n: int) -> list[int]:
    res = []
    i = 1

    while i <= n:
        res.append(i)
        i += 1
    
    return res