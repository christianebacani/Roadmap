# 1669A - Division?

t = int(input().strip())

for _ in range(t):
    rating = int(input().strip())

    if rating >= 1900:
        print('Division 1')
    
    elif rating >= 1600 and rating <= 1899:
        print('Division 2')
    
    elif rating >= 1400 and rating <= 1599:
        print('Division 3')
    
    else:
        print('Division 4')