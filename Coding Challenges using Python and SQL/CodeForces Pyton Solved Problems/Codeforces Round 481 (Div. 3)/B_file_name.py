# B - File Name

def is_filename_contains_three_or_more_x(file_name: str) -> bool:
    for i in range(2, len(file_name)):
        if (file_name[i - 2] + file_name[i - 1] + file_name[i]) != 'xxx':
            continue

        return True
    
    return False

n = int(input().strip())
filename = input().strip()
total_characters_to_remove = 0

while is_filename_contains_three_or_more_x(filename) is True:
    for i in range(2, len(filename)):
        if (filename[i - 2] + filename[i - 1] + filename[i]) != 'xxx':
            continue

        filename = filename[:i - 2] + filename[i - 1:]
        total_characters_to_remove += 1
        break

print(total_characters_to_remove)