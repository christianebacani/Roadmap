# Question: Friend or Foe?
# Categories: 7 Kyu

def friend(x: list[str]) -> list[str]:
    friends = []

    for i in range(len(x)):
        if len(x[i]) == 4:
            friends.append(x[i])
    
    return friends