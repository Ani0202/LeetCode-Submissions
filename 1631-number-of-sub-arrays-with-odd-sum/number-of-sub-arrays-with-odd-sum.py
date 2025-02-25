class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        total = 0
        even = 1
        odd = 0
        ans = 0
        for num in arr:
            if num % 2:
                if total:
                    ans = (ans + odd) % 1000000007
                    total = 0
                    even += 1
                else:
                    ans = (ans + even) % 1000000007
                    total = 1
                    odd += 1
            else:
                if total:
                    ans = (ans + even) % 1000000007
                    total = 1
                    odd += 1
                else:
                    ans = (ans + odd) % 1000000007
                    total = 0
                    even += 1

        return ans
