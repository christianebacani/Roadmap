# 313A - Ilya and Bank Account

n = input().strip()
possible_maximum_state_of_bank_account = [int(n), int(n[:-1]), int(n[:-2] + n[-1])]

print(max(possible_maximum_state_of_bank_account))