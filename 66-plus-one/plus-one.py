class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        ans = []
        n = 1
        for i in digits[::-1]:
            ans.append((i + n) % 10)
            n = (n + i) // 10

        if n:
            ans.append(n)

        return ans[::-1]
