# 3274.) Check if Two Chessboard Squares Have the Same Color
# Categories: Math, String

class Solution:
    def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:
        chess_board_squares_are_white = {
            'a': [2, 4, 6, 8],
            'b': [1, 3, 5, 7],
            'c': [2, 4, 6, 8],
            'd': [1, 3, 5, 7],
            'e': [2, 4, 6, 8],
            'f': [1, 3, 5, 7],
            'g': [2, 4, 6, 8],
            'h': [1, 3, 5, 7]
        }

        chess_board_squares_of_black = {
            'a': [1, 3, 5, 7],
            'b': [2, 4, 6, 8],
            'c': [1, 3, 5, 7],
            'd': [2, 4, 6, 8],
            'e': [1, 3, 5, 7],
            'f': [2, 4, 6, 8],
            'g': [1, 3, 5, 7],
            'h': [2, 4, 6, 8]
        }
        
        if (int(coordinate1[1]) in chess_board_squares_of_black[coordinate1[0]]) and (int(coordinate2[1]) in chess_board_squares_of_black[coordinate2[0]]):
            return True

        if (int(coordinate1[1]) in chess_board_squares_are_white[coordinate1[0]]) and (int(coordinate2[1]) in chess_board_squares_are_white[coordinate2[0]]):
            return True
        
        return False
