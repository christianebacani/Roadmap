# 1579A - Casimir's String Solitaire

number_of_test_cases = int(input().strip())

for _ in range(number_of_test_cases):
    casimirs_string = input().strip()

    while ('A' in casimirs_string and 'B' in casimirs_string) or ('B' in casimirs_string and 'C' in casimirs_string):
        if 'A' in casimirs_string and 'B' in casimirs_string:
            for i in range(len(casimirs_string)):
                if casimirs_string[i] != 'A':
                    continue

                casimirs_string = casimirs_string[:i] + casimirs_string[i + 1:]
                break
                
            for i in range(len(casimirs_string)):
                if casimirs_string[i] != 'B':
                    continue

                casimirs_string = casimirs_string[:i] + casimirs_string[i + 1:]
                break
        
        else:
            for i in range(len(casimirs_string)):
                if casimirs_string[i] != 'B':
                    continue
                
                casimirs_string = casimirs_string[:i] + casimirs_string[i + 1:]
                break
            
            for i in range(len(casimirs_string)):
                if casimirs_string[i] != 'C':
                    continue
                
                casimirs_string = casimirs_string[:i] + casimirs_string[i + 1:]
                break        

    if casimirs_string == '':
        print('YES')
    
    else:
        print('NO')