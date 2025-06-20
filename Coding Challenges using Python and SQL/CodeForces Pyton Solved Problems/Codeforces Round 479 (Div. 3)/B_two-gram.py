# B - Two-gram

n = input()
grams = input().strip()

two_grams_and_frequency = {}

for i in range(1, len(grams)):
    two_gram = grams[i - 1:i + 1]
    count = 0

    for i in range(1, len(grams)):
        if two_gram == grams[i - 1:i + 1]:
            count += 1

    two_grams_and_frequency[two_gram] = count

maximum_frequency = max(two_grams_and_frequency.values())

for two_gram, frequency in two_grams_and_frequency.items():
    if maximum_frequency == frequency:
        print(two_gram)
        break