# 133A - HQ9+

p = input().strip()
programs_that_produces_output = ['H', 'Q', '9']
program_will_produce_output = False

for i in range(len(programs_that_produces_output)):
    if programs_that_produces_output[i] in p:
        program_will_produce_output = True

if program_will_produce_output:
    print('YES')

else:
    print('NO')