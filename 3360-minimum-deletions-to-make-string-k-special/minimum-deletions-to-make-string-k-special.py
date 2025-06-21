class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        hmap = defaultdict(int)
        for letter in word:
            hmap[letter] += 1

        ans = len(word)
        for i in hmap.values():
            temp = 0
            for j in hmap.values():
                if i > j:
                    temp += j
                elif j > i + k:
                    temp += j - (i + k)

            ans = min(ans, temp)

        return ans
