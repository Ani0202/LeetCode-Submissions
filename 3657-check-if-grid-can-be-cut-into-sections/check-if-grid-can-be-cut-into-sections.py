class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        rectangles.sort()
        prev = rectangles[0][2]
        find = 0
        for startx, _, endx, _ in rectangles[1:]:
            if startx >= prev:
                find += 1
            prev = max(prev, endx)
            if find == 2:
                return True

        rectangles.sort(key=lambda x: x[1])
        prev = rectangles[0][3]
        find = 0
        for _, starty, _, endy in rectangles[1:]:
            if starty >= prev:
                find += 1
            prev = max(prev, endy)
            if find == 2:
                return True

        return False
