class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        mod = 10**9 + 7
        arr.sort()
        valueIndex = {value: index for index, value in enumerate(arr)}

        dp = [1 for _ in range(len(arr))]

        for i, num1 in enumerate(arr):
            for j in range(i):
                num2 = arr[j]
                if num1 % num2 == 0:
                    num3 = num1 // num2

                    if num3 in valueIndex:
                        dp[i] = (dp[i] + dp[j] * dp[valueIndex[num3]]) % mod

        return sum(dp) % mod
