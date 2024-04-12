class Solution:
    def minimumPushes(self, word: str) -> int:
        hmap = Counter(word)
        ans = 0
        sortedHmap = sorted(hmap.values(), reverse=True)
        for i, v in enumerate(sortedHmap):
            ans += ((i // 8) + 1) * v

        return ans
