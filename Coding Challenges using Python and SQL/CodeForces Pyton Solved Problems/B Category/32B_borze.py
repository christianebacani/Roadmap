# 32B - Borze

borze_code = input().strip()
borze_code = borze_code.replace('--', '2')
borze_code = borze_code.replace('-.', '1')
borze_code = borze_code.replace('.', '0')
print(borze_code)