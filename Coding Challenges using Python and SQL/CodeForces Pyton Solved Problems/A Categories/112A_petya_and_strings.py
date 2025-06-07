# 112A - Petya and Strings

first_string = input().strip().lower()
second_string = input().strip().lower()

if first_string < second_string:
    print(-1)

elif first_string > second_string:
    print(1)

else:
    print(0)