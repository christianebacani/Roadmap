# 2833.) Furthest Point From Origin
# Categories: String, Counting

class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        number_of_occurences_of_left_move = moves.count('L')
        number_of_occurences_of_right_move = moves.count('R')

        if number_of_occurences_of_left_move >= number_of_occurences_of_right_move:
            moves = moves.replace('_', 'L')

        else:
            moves = moves.replace('_', 'R')
        
        distance_from_origin = 0

        for i in range(len(moves)):
            if moves[i] == 'L':
                distance_from_origin -= 1
            
            else:
                distance_from_origin += 1
        
        return abs(distance_from_origin - 0)