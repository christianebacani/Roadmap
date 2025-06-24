# A - BerOS file system

path = input().strip().split('/')
normalized_path = []

for i in range(len(path)):
    if path[i] == '':
        continue

    normalized_path.append(path[i])

normalized_path = '/' + ('/'.join(normalized_path))
print(normalized_path)