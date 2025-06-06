# 71A - Way Too Long Words

number_of_words = int(input())

for _ in range(number_of_words):
    word = input()

    if len(word) > 10:
        answer = word[0] + str(len(word[1:-1])) + word[-1]

    else:
        answer = word

    print(answer)