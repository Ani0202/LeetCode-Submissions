class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        ans = []
        for i in range(1, 9):
            temp = i
            for j in range(i + 1, 10):
                temp = temp * 10 + j
                if low <= temp <= high:
                    ans.append(temp)
        return sorted(ans)
