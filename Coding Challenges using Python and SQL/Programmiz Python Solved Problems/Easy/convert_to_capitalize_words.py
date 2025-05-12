# Write a function to convert a given string to title case
# Categories: Easy

def convert_to_titlecase(s: str):
    s = s.split()

    for i in range(len(s)):
        s[i] = s[i].capitalize()
    
    return ' '.join(s)