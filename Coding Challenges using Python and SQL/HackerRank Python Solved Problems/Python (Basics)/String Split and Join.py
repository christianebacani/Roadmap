# Question Name : String Split and Join
# Category Name : Python (Basics)
# Sub-Category Name : Strings


# Function to split the string and join using '-'
def split_and_join(line):
    splittedLine = line.split(" ")
    joinedLine = '-'.join(splittedLine)
    return joinedLine # Return the newly formed string/s


if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)



