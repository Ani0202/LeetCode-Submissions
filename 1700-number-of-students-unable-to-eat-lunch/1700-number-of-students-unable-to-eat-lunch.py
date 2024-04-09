class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        circle = 0
        square = 0
        for student in students:
            if student == 0:
                circle += 1
            else:
                square += 1

        for sandwich in sandwiches:
            if sandwich == 0:
                if circle == 0:
                    return square
                else:
                    circle -= 1
            else:
                if square == 0:
                    return circle
                else:
                    square -= 1

        return 0
