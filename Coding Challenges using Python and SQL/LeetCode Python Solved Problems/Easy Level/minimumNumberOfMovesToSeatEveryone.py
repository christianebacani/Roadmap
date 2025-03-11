# 2037.) Minimum Number of Moves to Seat Everyone
# Categories: Array, Greedy, Sorting, Counting Sort

class Solution:
    def minMovesToSeat(self, seats: list[int], students: list[int]) -> int:
        seats = sorted(seats)
        students = sorted(students)

        number_of_moves = 0

        for student_position, student in enumerate(students):
            for seat_position, seat in enumerate(seats):
                if (student_position == seat_position):
                    number_of_moves += abs(student - seat)
    
        return number_of_moves
