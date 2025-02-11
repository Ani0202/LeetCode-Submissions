class Solution:
    def maximizeSquareHoleArea(
        self, n: int, m: int, hBars: List[int], vBars: List[int]
    ) -> int:
        hBars.sort()
        vBars.sort()

        def findCons(bars):
            if len(bars) == 0:
                return 0

            ans = 1
            temp = 1
            for i in range(1, len(bars)):
                if bars[i] == bars[i - 1] + 1:
                    temp += 1
                else:
                    ans = max(ans, temp)
                    temp = 1

            return max(ans, temp)

        hMax = findCons(hBars)
        vMax = findCons(vBars)
        return (min(hMax, vMax) + 1) ** 2
