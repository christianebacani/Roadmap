# A - Blackboard Game

t = int(input().strip())

for _ in range(t):
    n = int(input().strip())
    integers = [num for num in range(n)]
    alice_won = False
    bob_won = False

    while True:
        a = None

        if len(integers) > 0:
            a = integers[0]
            integers = integers[1:]
        
        if a is None:
            bob_won = True
            break
        
        b = None

        for i in range(len(integers)):
            if ((a + integers[i]) - 3) % 4 == 0:
                b = integers[i]
                integers = integers[:i] + integers[i + 1:]
                break
        
        if b is None:
            alice_won = True
            break
    
    if alice_won:
        print('Alice')
    
    else:
        print('Bob')