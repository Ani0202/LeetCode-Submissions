class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        ans = 0
        wordCount = dict()
        for word in words:
            revWord = word[::-1]
            if wordCount.get(revWord, 0):
                ans += 4
                wordCount[revWord] -= 1
            else:
                wordCount[word] = wordCount.get(word, 0) + 1

        for k, v in wordCount.items():
            if v != 0 and k == k[::-1]:
                ans += 2
                break

        return ans
