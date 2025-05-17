# Question: Complementary DNA
# Categories: 7 Kyu

def DNA_strand(dna):
    complements = {
        'A': 'T',
        'T': 'A',
        'C': 'G',
        'G': 'C'
    }
    dna = list(dna)

    for i in range(len(dna)):
        dna[i] = complements[dna[i]]

    dna = ''.join(dna)

    return dna