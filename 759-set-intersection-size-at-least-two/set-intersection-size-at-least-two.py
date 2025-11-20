class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        print(intervals)
        curr = []
        ans = 0
        for s, t in intervals:
            if not curr or curr[1] < s:
                ans += 2
                curr = [t - 1, t]
            elif curr[0] < s:
                if curr[1] != t:
                    curr = [curr[1], t]
                else:
                    curr = [t - 1, t]

                ans += 1

        return ans
