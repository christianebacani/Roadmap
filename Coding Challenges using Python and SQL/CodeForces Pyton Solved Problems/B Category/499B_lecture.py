# 499B - Lecture

test_input = input().strip().split()
n = int(test_input[0])
m = int(test_input[1])

first_language_and_second_language = {}

for _ in range(m):
    language = input().strip().split()
    first_language_and_second_language[language[0]] = language[1]

text_of_the_lecture = input().strip().split()

answer = []

for i in range(len(text_of_the_lecture)):
    for key, value in first_language_and_second_language.items():
        if text_of_the_lecture[i] != key:
            continue

        if len(key) <= len(value):
            answer.append(key)
        
        else:
            answer.append(value)
        
        break

print(' '.join(answer))