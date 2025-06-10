# 443A - Anton and Letters

set_of_letters = input().strip()
set_of_letters = set_of_letters.replace('{', '')
set_of_letters = set_of_letters.replace('}', '')
set_of_letters = set_of_letters.replace(', ', ' ')
print(len(set(set_of_letters.split())))