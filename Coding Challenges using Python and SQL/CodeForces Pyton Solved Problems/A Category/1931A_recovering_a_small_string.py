# 1931A - Recovering a Small String

alphabet = 'abcdefghijklmnopqrstuvwxyz'

t = int(input().strip())

for _ in range(t):
    encoded_word_value = int(input().strip())
    possible_encoded_words = []

    for i in range(len(alphabet)):
        for j in range(len(alphabet)):
            for k in range(len(alphabet)):
                if (i + 1) + (j + 1) + (k + 1) != encoded_word_value:
                    continue

                possible_encoded_words.append(alphabet[i] + alphabet[j] + alphabet[k])
    
    possible_encoded_words = sorted(possible_encoded_words)

    print(possible_encoded_words[0])