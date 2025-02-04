class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        ind = dict()
        for i, word in enumerate(words):
            ind[word] = i

        ans = []
        for i, word in enumerate(words):
            for j in range(len(word) + 1):
                left = word[:j]
                right = word[j:]
                revLeft = left[::-1]
                revRight = right[::-1]
                if revLeft in ind and ind[revLeft] != i and right == revRight:
                    ans.append([i, ind[revLeft]])

                if j > 0 and revRight in ind and ind[revRight] != i and left == revLeft:
                    ans.append([ind[revRight], i])

        return ans
