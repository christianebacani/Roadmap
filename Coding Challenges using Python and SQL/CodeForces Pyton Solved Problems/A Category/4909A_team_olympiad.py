# 490A - Team Olympiad

n = int(input().strip())
value_of_every_child = input().strip().split()
value_of_every_child = [int(value) for value in value_of_every_child]

children_that_is_good_at_programming = []
children_that_is_good_at_math = []
children_that_is_good_at_pe = []

for i in range(len(value_of_every_child)):
    if value_of_every_child[i] == 1:
        children_that_is_good_at_programming.append(i + 1)
    
    elif value_of_every_child[i] == 2:
        children_that_is_good_at_math.append(i + 1)

    else:
        children_that_is_good_at_pe.append(i + 1)

total_children = max([len(children_that_is_good_at_programming), len(children_that_is_good_at_math), len(children_that_is_good_at_pe)])
list_of_teams = []
w = 0

for i in range(total_children):
    try:
        team = [str(children_that_is_good_at_programming[i]), str(children_that_is_good_at_math[i]), str(children_that_is_good_at_pe[i])]

        if len(team) == 3:
            w += 1
            list_of_teams.append(team)

    except IndexError:
        continue

print(w)

for i in range(len(list_of_teams)):
    print(' '.join(list_of_teams[i]))