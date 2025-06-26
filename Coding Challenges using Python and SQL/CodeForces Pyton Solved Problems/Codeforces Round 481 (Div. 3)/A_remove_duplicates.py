# A - Remove Duplicates

n = int(input().strip())
array = input().strip().split()
array = [int(num) for num in array]

new_array = []

for i in range(len(array)):
    if array[i] in array[i + 1:]:
        continue
    
    if array[i] in new_array:
        continue

    new_array.append(array[i])

print(len(new_array))

new_array = [str(num) for num in new_array]
new_array = ' '.join(new_array)

print(new_array)