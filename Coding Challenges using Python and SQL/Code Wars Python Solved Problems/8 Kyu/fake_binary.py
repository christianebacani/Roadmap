# Question: Fake Binary
# Categories: 8 Kyu

def fake_bin(x: str) -> str:
    x = list(x)

    for i in range(len(x)):
        if int(x[i]) < 5:
            x[i] = '0'
        
        else:
            x[i] = '1'
    
    x = ''.join(x)

    return x