class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        nums_set = set(nums)
        n = len(nums)

        def find_str(temp):
            if len(temp) == n:
                if temp not in nums_set:
                    return temp

                return ""

            add_zero = find_str(temp + "0")
            if add_zero:
                return add_zero

            add_one = find_str(temp + "1")
            if add_one:
                return add_one

            return ""

        return find_str("")
