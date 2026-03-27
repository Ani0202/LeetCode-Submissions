class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        fruits_count = defaultdict(int)
        ans = 0
        i = 0
        j = 0
        while j < len(fruits):
            fruits_count[fruits[j]] += 1
            while len(fruits_count) > 2:
                fruits_count[fruits[i]] -= 1
                if fruits_count[fruits[i]] == 0:
                    del fruits_count[fruits[i]]
                i += 1

            ans = max(ans, j - i + 1)
            j += 1

        return ans
