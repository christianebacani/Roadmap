# 3222.) Find the Winning Player in Coin Game
# Categories: Math, Simulation, Game Theory

class Solution:
    def winningPlayer(self, x: int, y: int) -> str:
        player_name_turns = []
        number_of_turns = 0
        
        while x >= 1 and y >= 4:
            number_of_turns += 1
            x -= 1
            y -= 4
            
            if number_of_turns % 2 != 0:
                player_name_turns.append('Alice')
            
            else:
                player_name_turns.append('Bob')
            
        if player_name_turns == []:
            return 'Bob'
    
        return player_name_turns[-1]