class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        n = len(words)
        vowels = "aeiou"
        leftArr = [0 for _ in range(n)]
        if words[0][0] in vowels and words[0][-1] in vowels:
            leftArr[0] = 1
        for i in range(1, n):
            leftArr[i] = leftArr[i - 1] + (
                1 if (words[i][0] in vowels and words[i][-1] in vowels) else 0
            )

        m = len(queries)
        ans = [0 for _ in range(m)]
        for i in range(m):
            ans[i] = leftArr[queries[i][1]] - (
                leftArr[queries[i][0] - 1] if queries[i][0] != 0 else 0
            )

        return ans
