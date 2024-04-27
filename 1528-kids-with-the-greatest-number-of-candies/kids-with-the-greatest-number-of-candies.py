class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxCandies = max(candies)
        ans = []
        for num in candies:
            ans.append(num + extraCandies >= maxCandies)

        return ans
