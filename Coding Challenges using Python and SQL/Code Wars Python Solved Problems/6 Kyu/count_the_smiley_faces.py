# Question: Count the smiley faces!
# Categories: 6 Kyu

def count_smileys(arr: list[str]) -> int:
    count = 0

    for i in range(len(arr)):
        face = []

        for j in range(len(arr[i])):
            face.append(arr[i][j])

        if len(face) == 2 and face[0] in [':', ';'] and face[1] in [')', 'D']:
            count += 1
        
        elif len(face) == 3 and face[0] in [':', ';'] and face[1] in ['-', '~'] and face[2] in [')', 'D']:
            count += 1

    return count