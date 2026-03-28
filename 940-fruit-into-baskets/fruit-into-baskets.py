class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        fruits_count = defaultdict(int)
        i = 0
        for j in range(len(fruits)):
            fruits_count[fruits[j]] += 1
            if len(fruits_count) > 2:
                fruits_count[fruits[i]] -= 1
                if fruits_count[fruits[i]] == 0:
                    del fruits_count[fruits[i]]

                i += 1

        return len(fruits) - i
