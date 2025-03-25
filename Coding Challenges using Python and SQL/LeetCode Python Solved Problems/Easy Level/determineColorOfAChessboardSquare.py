# 1812.) Determine Color of a Chessboard Square
# Categories: Math, String

class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        chess_squares_of_black = {
            'a': [1, 3, 5, 7],
            'b': [2, 4, 6, 8],
            'c': [1, 3, 5, 7],
            'd': [2, 4, 6, 8],
            'e': [1, 3, 5, 7],
            'f': [2, 4, 6, 8],
            'g': [1, 3, 5, 7],
            'h': [2, 4, 6, 8]
        }
    
        if int(coordinates[1]) in chess_squares_of_black[coordinates[0]]:
            return False
        
        return True
    