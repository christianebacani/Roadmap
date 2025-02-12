# 2878.) Get the Size of a Dataframe
# Category : Pandas

import pandas as pd

def getDataframeSize(players: pd.DataFrame) -> list[int]:
    rowSize = len(players['player_id'])
    columnSize = len(players.keys())
    
    return [rowSize, columnSize]
