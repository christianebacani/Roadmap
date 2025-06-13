# B - Ten Words of Wisdom

t = int(input().strip())

for _ in range(t):
    n = int(input().strip())
    words_and_quality = []

    for _ in range(n):
        user_input = input().strip().split()
        words_and_quality.append([int(user_input[0]), int(user_input[1])])
    
    maximum_quality_that_words_not_greater_than_ten = 0

    for i in range(len(words_and_quality)):
        if words_and_quality[i][0] <= 10 and words_and_quality[i][1] > maximum_quality_that_words_not_greater_than_ten:
            maximum_quality_that_words_not_greater_than_ten = words_and_quality[i][1]
    
    for i in range(len(words_and_quality)):
        if words_and_quality[i][0] <= 10 and words_and_quality[i][1] == maximum_quality_that_words_not_greater_than_ten:
            print(i + 1)
            break