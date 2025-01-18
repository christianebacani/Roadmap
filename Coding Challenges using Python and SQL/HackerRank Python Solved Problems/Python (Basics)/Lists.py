# Question Name : 'Lists'
# Exercise Category : Python (Basic)
# Exercise Sub Category : Python Basic Data Types

if __name__ == '__main__':
    N = int(input())

    lst = []

    for i in range(N):
        commands = input()
        
        if "insert" in commands:
            newElement = int(commands[-2:])
            index = int(commands[7:9])
            lst.insert(index, newElement)

        elif "print" in commands:
            print(lst)

        elif "remove" in commands:
            element = int(commands[-2:])

            for index, i in enumerate(lst):
                if i == element:
                    lst.pop(index)
                    break
            
        elif "append" in commands:
            element = int(commands[-2:])
            lst.append(element)
            
        elif "sort" in commands:
            lst = sorted(lst)
            
        elif "pop" in commands:
            lst.pop(-1)
            
        elif "reverse" in commands:
            lst = lst[::-1]

        else:
            pass

