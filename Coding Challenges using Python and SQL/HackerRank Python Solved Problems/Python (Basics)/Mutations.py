# Question Name : Mutations
# Category Name : Python (Basics)
# Sub-Categogory : Strings

def mutate_string(string, position, character):
    lst = list(string) # Convert to list (mutable object)
    lst[position] = character # Modify
    return ''.join(lst) # Convert to string the modified list

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)