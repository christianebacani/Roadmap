# Question Name : What's your name?
# Category Name : Python (Basic)
# Sub-Category Name : Strings

# Display full name
def print_full_name(first, last):
    welcomeMessage =  f'Hello {first} {last}! You just delved into python.'
    print(welcomeMessage)


if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)


