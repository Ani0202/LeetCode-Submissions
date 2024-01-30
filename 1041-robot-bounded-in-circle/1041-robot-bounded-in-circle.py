class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        x = 0
        y = 0
        dirc = 0
        for i in instructions:
            if i == "R":
                dirc = (dirc + 1) % 4
            elif i == "L":
                dirc = (dirc + 3) % 4
            else:
                if dirc == 0:
                    y += 1
                elif dirc == 1:
                    x += 1
                elif dirc == 2:
                    y -= 1
                else:
                    x -= 1
        if (x == 0 and y == 0) or dirc != 0:
            return True
        return False
