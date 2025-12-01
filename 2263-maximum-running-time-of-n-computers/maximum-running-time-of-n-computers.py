class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        low = min(batteries)
        high = sum(batteries)
        ans = -1
        while low <= high:
            mid = (low + high) // 2
            total_charge = 0
            charge_needed = n * mid
            for charge in batteries:
                total_charge += min(mid, charge)
                if total_charge >= charge_needed:
                    break

            if total_charge >= charge_needed:
                ans = mid
                low = mid + 1
            else:
                high = mid - 1

        return ans
