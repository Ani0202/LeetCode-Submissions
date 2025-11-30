class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        n = len(nums)
        target_rem = 0
        for num in nums:
            target_rem = (target_rem + num) % p

        if target_rem == 0:
            return 0

        rems = {0: -1}
        current_rem = 0
        ans = n
        for i, num in enumerate(nums):
            current_rem = (current_rem + num) % p
            remove_rem = (current_rem - target_rem + p) % p
            if remove_rem in rems:
                ans = min(ans, i - rems[remove_rem])

            rems[current_rem] = i

        if ans == n:
            return -1

        return ans
