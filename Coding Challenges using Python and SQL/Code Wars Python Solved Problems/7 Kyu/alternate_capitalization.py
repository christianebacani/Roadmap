# Question: Alternate capitalization
# Categories: 7 Kyu

def capitalize(s: str) -> list[str]:
    even_indexed_capitalization, odd_indexed_capitalization = '', ''

    for i in range(len(s)):
        if i % 2 == 0:
            even_indexed_capitalization += s[i].upper()
        
        else:
            even_indexed_capitalization += s[i]
    
    for i in range(len(s)):
        if i % 2 != 0:
            odd_indexed_capitalization += s[i].upper()
        
        else:
            odd_indexed_capitalization += s[i]
    
    return [even_indexed_capitalization, odd_indexed_capitalization]