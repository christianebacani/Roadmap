# 34A - Reconnaissance 2

n = input().strip()
height_of_soldiers = input().strip().split()
height_of_soldiers = [int(height) for height in height_of_soldiers]

differences = []

for i in range(len(height_of_soldiers)):
    if i == (len(height_of_soldiers) - 1):
        differences.append(abs(height_of_soldiers[i] - height_of_soldiers[0]))
    
    else:
        differences.append(abs(height_of_soldiers[i] - height_of_soldiers[i + 1]))

for i in range(len(height_of_soldiers)):
    if i == (len(height_of_soldiers) - 1) and abs(height_of_soldiers[i] - height_of_soldiers[0]) == min(differences):
        print(f'{i + 1} {1}')
        break

    elif i != (len(height_of_soldiers) - 1) and abs(height_of_soldiers[i] - height_of_soldiers[i + 1]) == min(differences):
        print(f'{i + 1} {i + 2}')
        break

    else:
        pass