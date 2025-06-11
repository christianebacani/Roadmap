# 61A - Ultra-Fast Mathematician

first_number = input().strip()
second_number = input().strip()
total_length = len(first_number)
result = ''

for i in range(total_length):
    if first_number[i] != second_number[i]:
        result += '1'

    else:
        result += '0'

answer = result
print(answer)