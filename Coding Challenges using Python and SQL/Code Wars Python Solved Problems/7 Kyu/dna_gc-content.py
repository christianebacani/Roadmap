# Question: DNA GC-content
# Categories: 7 Kyu

def gc_content(seq: str) -> float:
    frequency_of_guanine_content = seq.count('G')
    frequency_of_cytosine_content = seq.count('C')

    try:
        return ((frequency_of_guanine_content + frequency_of_cytosine_content) / len(seq)) * 100
    
    except ZeroDivisionError:
        return 0.0