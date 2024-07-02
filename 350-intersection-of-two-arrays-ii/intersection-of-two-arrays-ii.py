class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        nums1.sort()
        nums2.sort()
        i = 0
        j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] <= nums2[j]:
                if nums1[i] == nums2[j]:
                    ans.append(nums1[i])
                    j += 1
                i += 1
            else:
                j += 1

        return ans
