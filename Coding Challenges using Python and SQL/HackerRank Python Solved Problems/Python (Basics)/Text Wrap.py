# Question Name : Text Wrap
# Category Name : Python (Basics)
# Sub-Category Name : Strings

import textwrap

def wrap(string, max_width):
    wrapper = textwrap.TextWrapper(width=max_width) # Define the width to wrap the string value
    
    word_list = wrapper.wrap(text=string) # Text Wrapping the string values with specific width using textwrap module

    return '\n'.join(word_list) # Return the elements that is separated with newline


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
