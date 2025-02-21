class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        vowelToInt = {"a": 0, "e": 1, "i": 2, "o": 3, "u": 4}
        appear = {word[0]}
        i = 0
        ans = 0
        for j in range(1, len(word)):
            if vowelToInt[word[j]] < vowelToInt[word[j - 1]]:
                if len(appear) == 5:
                    ans = max(ans, j - i)

                i = j
                appear = {word[j]}

            else:
                appear.add(word[j])

        if len(appear) == 5:
            ans = max(ans, j - i + 1)

        return ans
