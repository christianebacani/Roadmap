# Question: Online RPG: player to qualifying stage?
# Categories: 8 Kyu

def playerRankUp(pts: int) -> bool | str:
    if pts >= 100:
        return 'Well done! You have advanced to the qualifying stage. Win 2 out of your next 3 games to rank up.'

    return False