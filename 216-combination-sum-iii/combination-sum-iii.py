class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        self.ans = []

        def backTrack(temp, start):
            if len(temp) == k and sum(temp) == n:
                self.ans.append(temp[:])
            elif len(temp) >= k or sum(temp) > n:
                return
            else:
                for i in range(start, 10):
                    temp.append(i)
                    backTrack(temp, i + 1)
                    temp.pop()

        backTrack([], 1)
        return self.ans
