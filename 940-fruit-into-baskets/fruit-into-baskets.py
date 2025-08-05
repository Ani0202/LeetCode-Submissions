class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        fruitsSelected = defaultdict(int)
        i = 0
        ans = 0
        for j in range(len(fruits)):
            fruitsSelected[fruits[j]] += 1
            while len(fruitsSelected) > 2:
                fruitsSelected[fruits[i]] -= 1
                if fruitsSelected[fruits[i]] == 0:
                    del fruitsSelected[fruits[i]]

                i += 1

            ans = max(ans, j - i + 1)

        return ans
