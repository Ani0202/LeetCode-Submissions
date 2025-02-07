class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        remArr = [0] * k
        remArr[0] = 1
        ans = 0
        count = 0
        for num in nums:
            count += num
            rem = count % k
            ans += remArr[rem]
            remArr[rem] += 1

        return ans
