# 2036A - Quintomania

t = int(input().strip())

for _ in range(t):
    n = int(input().strip())
    notes = input().strip().split()
    notes = [int(note) for note in notes]

    the_melody_is_perfect = True

    for i in range(1, len(notes)):
        semitone = abs(notes[i - 1] - notes[i])

        if semitone in [5, 7]:
            continue

        the_melody_is_perfect = False
        break

    if the_melody_is_perfect:
        print('YES')
    
    else:
        print('NO')