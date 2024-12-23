class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for i in range(32):
            temp = 0
            for num in nums:
                if num < 0:
                    num = num & (2**32-1)
                temp += (num >> i) & 1
            temp %= 3
            ans |= temp << i

        if ans >= 2**31:
            ans -= 2**32
        return ans
