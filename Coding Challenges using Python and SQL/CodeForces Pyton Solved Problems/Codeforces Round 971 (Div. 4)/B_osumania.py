# B - osu!mania

t = input().strip()

for _ in range(int(t)):
    n = int(input().strip())
    beatmap = []

    for _ in range(n):
        beatmap.append(input().strip())
    
    beatmap = beatmap[::-1]
    columns_that_notes_appears_per_row = []

    for i in range(len(beatmap)):
        for j in range(len(beatmap[i])):
            if beatmap[i][j] == '#':
                columns_that_notes_appears_per_row.append(str(j + 1))
                break
    
    print(' '.join(columns_that_notes_appears_per_row))