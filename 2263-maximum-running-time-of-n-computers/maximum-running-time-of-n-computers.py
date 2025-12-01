class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        low = min(batteries)
        high = sum(batteries)
        ans = -1
        while low <= high:
            mid = (low + high) // 2
            total_charge = 0
            for charge in batteries:
                total_charge += min(mid, charge)

            if total_charge >= n * mid:
                ans = mid
                low = mid + 1
            else:
                high = mid - 1

        return ans