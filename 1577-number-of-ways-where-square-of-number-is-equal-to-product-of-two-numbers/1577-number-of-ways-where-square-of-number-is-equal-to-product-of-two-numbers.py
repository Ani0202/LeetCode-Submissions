class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        def countTriplets(A, B):
            res = 0
            count = Counter(B)

            for i in A:
                target = i * i
                for j, freq in count.items():
                    if target % j > 0 or target // j not in count:
                        continue
                    if target // j == j:
                        res += freq * (freq - 1)
                    else:
                        res += freq * count[target // j]

            return res // 2

        return countTriplets(nums1, nums2) + countTriplets(nums2, nums1)
