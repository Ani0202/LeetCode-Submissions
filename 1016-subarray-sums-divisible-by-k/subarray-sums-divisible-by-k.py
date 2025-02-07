class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        remArr = [0] * k
        ans = 0
        count = 0
        for num in nums:
            count += num
            rem = count % k
            if rem == 0:
                ans += 1

            ans += remArr[rem]
            remArr[rem] += 1

        return ans
