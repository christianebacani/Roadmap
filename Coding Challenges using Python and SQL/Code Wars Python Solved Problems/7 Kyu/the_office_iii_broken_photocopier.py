# Question: The Office III - Broken Photocopier
# Categories: 7 Kyu

def broken(inp: str) -> str:
    inp = ['0' if i == '1' else '1' for i in list(inp)]
    return ''.join(inp)