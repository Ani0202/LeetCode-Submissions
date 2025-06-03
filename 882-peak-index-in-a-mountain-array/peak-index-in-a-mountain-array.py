class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l = 0
        h = len(arr) - 1
        while l <= h:
            m = l + (h - l) // 2
            left = arr[m - 1]
            right = arr[m + 1]
            print(l, m, h)
            if left < arr[m] and arr[m] > right:
                return m
            elif left < arr[m] < right:
                l = m
            else:
                h = m

        return -1
