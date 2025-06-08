# 59A - Word

word = input().strip()
number_of_lowercase = 0
number_of_uppercase = 0

for i in range(len(word)):
    if word[i].islower():
        number_of_lowercase += 1
    
    else:
        number_of_uppercase += 1

if number_of_uppercase > number_of_lowercase:
    print(word.upper())

else:
    print(word.lower())