class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        indexMap = dict()
        for i, letter in enumerate(s):
            indexMap[letter] = i

        permDiff = 0
        for i, letter in enumerate(t):
            permDiff += abs(i - indexMap[letter])

        return permDiff
