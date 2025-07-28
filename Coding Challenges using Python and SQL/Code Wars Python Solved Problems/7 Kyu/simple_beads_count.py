# Question: Simple beads count
# Categories: 7 Kyu

def count_red_beads(n):
    if n < 2:
        return 0
    
    beads = []

    for _ in range(n):
        beads.append('1')

    beads = '00'.join(beads)
    answer = beads.count('0')

    return answer