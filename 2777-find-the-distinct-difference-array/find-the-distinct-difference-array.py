class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        pref = dict()
        suff = dict()
        for num in nums:
            suff[num] = suff.get(num, 0) + 1

        diff_arr = []
        for num in nums:
            pref[num] = pref.get(num, 0) + 1
            suff[num] -= 1
            if suff[num] == 0:
                del suff[num]

            diff_arr.append(len(pref) - len(suff))

        return diff_arr
