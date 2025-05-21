class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        unusedWords = defaultdict(int)
        count = 0
        for word in words:
            revWord = word[::-1]
            if unusedWords[revWord] > 0:
                unusedWords[revWord] -= 1
                count += 4
            else:
                unusedWords[word] += 1

        for k, v in unusedWords.items():
            if k == k[::-1] and v > 0:
                count += 2
                break

        return count
