# Question: Did we win the Super Bowl?
# Categories: 7 Kyu

def did_we_win(plays: list[list[int, str]]) -> bool:
    yards = 0

    for i in range(len(plays)):
        if plays[i] == []:
            continue
        
        if plays[i][1] == 'turnover':
            return False
        
        if plays[i][1] in ['run', 'pass']:
            yards += plays[i][0]
        
        else:
            yards -= plays[i][0]
    
    if yards > 10:
        return True
    
    return False