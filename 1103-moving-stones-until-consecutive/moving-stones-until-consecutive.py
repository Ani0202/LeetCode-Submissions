class Solution:
    def numMovesStones(self, a: int, b: int, c: int) -> List[int]:
        pos = sorted([a, b, c])
        left = pos[0]
        middle = pos[1]
        right = pos[2]

        ans = [0, 0]

        if right - left <= 2:
            return ans

        if middle - left <= 2 or right - middle <= 2:
            ans[0] = 1
        else:
            ans[0] = 2

        ans[1] = right - left - 2

        return ans
